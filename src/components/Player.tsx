import { GlobalStates } from "../GlobalStates";
import "../styles/components/Player.scss";
import { useRef, useEffect, useContext, useState, useCallback } from "react";
import { GlobalStatesContext } from "../types";
import dayjs from "dayjs";
import Slider from "@mui/material/Slider";
import duration from "dayjs/plugin/duration";
import { Icons } from "./Icons";
import { usePlayerStorage } from "../hooks/usePlayerStorage";
import { useAudioState } from "../hooks/useAudioState";
import { useProgressBar } from "../hooks/useProgressBar";
import { useAudioEvents } from "../hooks/useAudioEvents";
import { useAutoScroll } from "../hooks/useAutoScroll";
import { SCROLL_DURATIONS } from "../constants/scrollConfig";

dayjs.extend(duration);
const Player = () => {
  const {
    lang,
    playlist,
    playing,
    setPlaying,
    setPlayOptions,
    qari,
    moshaf,
    setPageWidth,
    isLoading,
    setIsLoading,
    extensionMode,
    storageKey,
    pageWidth,
  } = useContext<GlobalStatesContext>(GlobalStates);

  const { getStoredData, updateStoredData } = usePlayerStorage(storageKey);
  const storedData = getStoredData();

  // Add auto-scroll functionality for smooth navigation
  const { scrollToCurrentItem } = useAutoScroll({
    playlist,
    playing,
    pageWidth,
  });

  const playerRef = useRef<HTMLDivElement>(null);
  const playBtnRef = useRef<HTMLButtonElement>(null);
  const nextBtnRef = useRef<HTMLButtonElement>(null);
  const audioRef = useRef<HTMLAudioElement>(null);
  const componentLoadedRef = useRef<boolean>(false);
  const loopStateRef = useRef<boolean>(storedData.loop || false);
  const playBtnTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);
  const progressUpdateInterval = useRef<ReturnType<typeof setInterval> | null>(
    null
  );

  const [isDragging, setIsDragging] = useState(false);
  const [hoverVolume, setHoverVolume] = useState(false);
  const wasPlayingBeforeDragRef = useRef(false);
  const volumePanelTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);

  const { audioState, setAudioState, playingStateRef, playAudio, pauseAudio } =
    useAudioState({
      storageKey,
      extensionMode,
      onPlayingChange: undefined, // Remove this callback to prevent circular updates
    });

  const {
    containerRef,
    pointerRef,
    progressRef,
    resetProgress,
    updateProgressPosition,
  } = useProgressBar({
    lang,
    audioState,
    onProgressChange: (time) => {
      if (!audioRef.current || !audioState) return;
      const audio = audioRef.current;
      audio.currentTime = time;
      pauseAudio(audio);
      setAudioState({ ...audioState, playing: false });

      // Resume playback after a short delay
      setTimeout(() => {
        if (!audioRef.current) return;
        playAudio(audioRef.current);
        setAudioState({ ...audioState, playing: true });
      }, 50);
    },
  });

  useAudioEvents({
    audioRef,
    playingStateRef,
    onLoadingChange: setIsLoading,
    onPlaybackError: () => {
      if (navigator.onLine && audioRef.current) {
        audioRef.current.load();
      }
    },
  });

  const [audioVolume, setAudioVolume] = useState(
    storedData.volume ? storedData.volume * 100 : 60
  );
  const [loop, setLoop] = useState(storedData.loop || false);

  // Helper function to position pointer based on language
  const positionPointer = useCallback(
    (pointer: HTMLDivElement, x: number, isRtl: boolean) => {
      if (isRtl) {
        pointer.style.right = `${x}px`;
        pointer.style.left = "auto";
      } else {
        pointer.style.left = `${x}px`;
        pointer.style.right = "auto";
      }
    },
    []
  );

  // Handle metadata load
  const onMetaDataLoad = useCallback(() => {
    if (!audioRef.current || !progressRef.current || !pointerRef.current)
      return;

    const audio = audioRef.current;

    // Set initial time from storage
    if (!componentLoadedRef.current) {
      const stored = localStorage.getItem(storageKey);
      const storedData = stored ? JSON.parse(stored) : {};
      audio.currentTime =
        "currentTime" in storedData ? storedData.currentTime : 0;

      // Don't auto-play, just set the state
      playingStateRef.current = false;
      audio.pause();
      componentLoadedRef.current = true;
    }

    const progress = progressRef.current;
    const pointer = pointerRef.current;
    const isRtl = lang === "ar";

    // Set initial state based on stored data
    const isInitiallyPlaying = !storedData.paused;
    setAudioState({
      playing: isInitiallyPlaying,
      duration: audio.duration,
    });
    setPlayOptions({
      playing: isInitiallyPlaying,
      duration: audio.duration,
      currentTime: audio.currentTime,
    });

    if (playingStateRef.current) {
      playAudio(audio);
      progress.style.width = "0";
      positionPointer(pointer, -5, isRtl);
    } else {
      pauseAudio(audio);
    }

    // Clear loading state once metadata is loaded and ready to play
    setIsLoading(false);
  }, [
    positionPointer,
    pauseAudio,
    playAudio,
    playingStateRef,
    pointerRef,
    progressRef,
    setAudioState,
    setIsLoading,
    setPlayOptions,
    storageKey,
    storedData.paused,
  ]);

  // Handle click on progress bar
  const onMouseClick = useCallback(
    (e: React.MouseEvent<HTMLDivElement>) => {
      if (
        !containerRef.current ||
        !pointerRef.current ||
        !progressRef.current ||
        !audioRef.current ||
        !audioState ||
        !playBtnRef.current ||
        !audioRef.current.duration
      ) {
        e.preventDefault();
        e.stopPropagation();
        return;
      }

      const pointer = pointerRef.current;
      const container = containerRef.current;
      const progressBar = progressRef.current;
      const audio = audioRef.current;
      const containerRect = container.getBoundingClientRect();
      const maxX = containerRect.width;
      const isRtl = lang === "ar";

      const { duration } = audioState;
      let clickX;

      if (isRtl) {
        clickX = containerRect.right - e.clientX;
      } else {
        clickX = e.clientX - containerRect.left;
      }

      const audioProgress = (clickX / maxX) * 100;

      // Immediately update pointer and progress without transition
      pointer.style.transition = "none";
      progressBar.style.transition = "none";
      positionPointer(pointer, clickX - 5, isRtl);
      progressBar.style.width = `${audioProgress}%`;

      // Store the playing state before pausing
      const wasPlaying = audioState.playing;

      // Set new audio time
      audio.currentTime = (duration * audioProgress) / 100;
      pauseAudio(audio);
      setAudioState({ ...audioState, playing: false });

      // Update playOptions immediately for Surah component sync
      setPlayOptions({
        playing: false,
        currentTime: audio.currentTime,
        duration: audio.duration,
      });

      // Resume playback after a very short delay if it was playing
      if (playBtnTimeout.current) {
        clearTimeout(playBtnTimeout.current);
      }
      playBtnTimeout.current = setTimeout(() => {
        // Resume if we were playing before seeking
        if (wasPlaying) {
          playAudio(audio);
          setAudioState({ ...audioState, playing: true });
        }
        // Restore transitions after playback resumes
        pointer.style.transition = "opacity 300ms ease-out";
        progressBar.style.transition = "width 100ms linear";
      }, 50);
    },
    [
      audioState,
      lang,
      positionPointer,
      containerRef,
      pauseAudio,
      playAudio,
      pointerRef,
      progressRef,
      setAudioState,
      setPlayOptions,
    ]
  );

  // Handle mouse move during drag
  const onMouseMove = useCallback(
    (e: MouseEvent) => {
      if (
        !containerRef.current ||
        !pointerRef.current ||
        !progressRef.current ||
        !audioRef.current ||
        !audioState ||
        !playBtnRef.current ||
        !isDragging
      )
        return;

      const pointer = pointerRef.current;
      const container = containerRef.current;
      const progressBar = progressRef.current;
      const audio = audioRef.current;
      const containerRect = container.getBoundingClientRect();
      const maxX = containerRect.width;
      const minX = 0;
      const isRtl = lang === "ar";

      const { duration } = audioState;
      let moveX;

      if (isRtl) {
        moveX = containerRect.right - e.clientX;
      } else {
        moveX = e.clientX - containerRect.left;
      }

      const clickX = Math.max(minX, Math.min(maxX, moveX));
      const audioProgress = (clickX / maxX) * 100;

      positionPointer(pointer, clickX - 5, isRtl);
      progressBar.style.width = `${audioProgress}%`;
      progressBar.style.transition = "none";

      // Set the new audio time
      audio.currentTime = (duration * audioProgress) / 100;

      // Update playOptions immediately for Surah component sync during drag
      setPlayOptions({
        playing: audioState.playing,
        currentTime: audio.currentTime,
        duration: audio.duration,
      });
    },
    [
      audioState,
      isDragging,
      lang,
      positionPointer,
      containerRef,
      pauseAudio,
      playAudio,
      pointerRef,
      progressRef,
      setAudioState,
      setPlayOptions,
    ]
  );

  // Reset progress bar when switching tracks
  useEffect(() => {
    resetProgress();
  }, [playlist[playing].src, lang, resetProgress]);

  // Update progress bar and pointer position
  useEffect(() => {
    if (
      !progressRef.current ||
      !pointerRef.current ||
      !audioRef.current ||
      !containerRef.current ||
      !audioState
    )
      return;

    const audio = audioRef.current;
    const container = containerRef.current;
    const isRtl = lang === "ar";

    // Only update if we have valid duration
    if (!audio.duration) {
      resetProgress();
      return;
    }

    const timeRemaining = (audio.duration - audio.currentTime) * 1000;
    const currentProgress = audio.currentTime / audio.duration;
    const containerRect = container.getBoundingClientRect();
    const maxX = containerRect.width;

    if (audioState.playing && !audio.paused && audio.readyState >= 3) {
      updateProgressPosition(
        progressRef.current,
        pointerRef.current,
        currentProgress,
        maxX,
        isRtl,
        timeRemaining
      );
    } else {
      updateProgressPosition(
        progressRef.current,
        pointerRef.current,
        currentProgress,
        maxX,
        isRtl
      );
    }
  }, [
    audioState,
    lang,
    resetProgress,
    updateProgressPosition,
    containerRef,
    pointerRef,
    progressRef,
  ]);

  // Add/remove mousemove and mouseup event listeners for dragging
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => onMouseMove(e);
    const handleMouseUp = () => {
      if (isDragging) {
        setIsDragging(false);

        // Resume playback if it was playing before drag
        if (wasPlayingBeforeDragRef.current && audioRef.current) {
          playAudio(audioRef.current);
          setAudioState((prev) => (prev ? { ...prev, playing: true } : null));
        }

        // Reset the ref
        wasPlayingBeforeDragRef.current = false;
      }
    };

    if (isDragging) {
      window.addEventListener("mousemove", handleMouseMove);
      window.addEventListener("mouseup", handleMouseUp);
    }

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
    };
  }, [isDragging, onMouseMove, playAudio, setAudioState]);

  // Reset the Slider on new Surah
  useEffect(() => {
    if (
      !pointerRef.current ||
      !progressRef.current ||
      !audioState ||
      !playBtnRef.current ||
      !audioRef.current
    )
      return;
    const pointer = pointerRef.current;
    const progress = progressRef.current;
    const isRtl = lang === "ar";

    progress.style.width = "0";

    if (isRtl) {
      pointer.style.right = `-5px`;
      pointer.style.left = "auto";
    } else {
      pointer.style.left = `-5px`;
      pointer.style.right = "auto";
    }

    progress.style.transition = "none";
    pointer.style.transition = "none";
    updateStoredData({
      paused: !playingStateRef.current,
      currentTime: audioRef.current.currentTime,
    });
    // Removed automatic play to prevent loops
  }, [
    playing,
    qari,
    moshaf,
    audioState,
    lang,
    playingStateRef,
    pointerRef,
    progressRef,
    updateStoredData,
  ]);
  useEffect(() => {
    if (
      !pointerRef.current ||
      !progressRef.current ||
      !audioState ||
      !playBtnRef.current ||
      !audioRef.current
    )
      return;
    const pointer = pointerRef.current;
    const progress = progressRef.current;
    const isRtl = lang === "ar";

    progress.style.width = "0";

    if (isRtl) {
      pointer.style.right = `-5px`;
      pointer.style.left = "auto";
    } else {
      pointer.style.left = `-5px`;
      pointer.style.right = "auto";
    }

    progress.style.transition = "none";
    pointer.style.transition = "none";
  }, [lang, audioState, pointerRef, progressRef]);

  // Update playOptions regularly when playing (for progress updates)
  useEffect(() => {
    if (audioState?.playing && audioRef.current) {
      progressUpdateInterval.current = setInterval(() => {
        const audio = audioRef.current;
        if (audio && !audio.paused) {
          setPlayOptions({
            playing: true,
            currentTime: audio.currentTime,
            duration: audio.duration || audioState.duration,
          });
        }
      }, 1000);
    } else {
      if (progressUpdateInterval.current) {
        clearInterval(progressUpdateInterval.current);
        progressUpdateInterval.current = null;
      }
    }

    return () => {
      if (progressUpdateInterval.current) {
        clearInterval(progressUpdateInterval.current);
        progressUpdateInterval.current = null;
      }
    };
  }, [audioState?.playing, audioState?.duration, setPlayOptions]);

  // Update playOptions when audioState changes (one-way sync to Surah component)
  useEffect(() => {
    if (audioState && audioRef.current) {
      setPlayOptions({
        playing: audioState.playing,
        currentTime: audioRef.current.currentTime,
        duration: audioState.duration,
      });
    }
  }, [audioState?.playing, audioState?.duration, setPlayOptions]);

  // Listen for external commands (from Surah component)
  useEffect(() => {
    const handlePlayerCommand = (event: CustomEvent) => {
      if (!audioRef.current || !audioState) return;

      const { action, surahIndex } = event.detail;
      const audio = audioRef.current;

      // If this is a different surah, switch to it first
      if (surahIndex !== undefined && surahIndex !== playing) {
        setPlaying(surahIndex);

        // Update localStorage for the track change
        updateStoredData({
          playing: surahIndex,
          currentTime: 0,
        });

        if (extensionMode) {
          chrome.runtime.sendMessage({
            type: "STOP_AUDIO",
          });
        }

        // If the action is play, we'll start playing the new track
        if (action === "play") {
          // The track change will trigger a re-render, and we'll start playing in the next cycle
          setTimeout(() => {
            if (audioRef.current) {
              playAudio(audioRef.current);
              setAudioState((prev) =>
                prev ? { ...prev, playing: true } : null
              );
            }
          }, 100);
        }
      } else {
        // Same surah, just handle play/pause
        if (action === "play" && !audioState.playing) {
          playAudio(audio);
          setAudioState((prev) => (prev ? { ...prev, playing: true } : null));
        } else if (action === "pause" && audioState.playing) {
          pauseAudio(audio);
          setAudioState((prev) => (prev ? { ...prev, playing: false } : null));
        }
      }
    };

    window.addEventListener(
      "playerCommand",
      handlePlayerCommand as EventListener
    );
    return () => {
      window.removeEventListener(
        "playerCommand",
        handlePlayerCommand as EventListener
      );
    };
  }, [
    audioState,
    playAudio,
    pauseAudio,
    setAudioState,
    playing,
    setPlaying,
    updateStoredData,
    extensionMode,
  ]);

  // Change the volume on slider move
  useEffect(() => {
    if (!audioRef.current) return;
    const audio = audioRef.current;
    audio.volume = audioVolume / 100;

    updateStoredData({ volume: audio.volume });

    if (extensionMode) {
      chrome.runtime.sendMessage({
        type: "CHANGE_VOLUME",
        volume: audio.volume,
      });
    }
  }, [audioVolume, extensionMode, updateStoredData]);

  // Handle Pointer Reposition on Window Resize
  useEffect(() => {
    const handleWindowResize = () => {
      if (!containerRef.current || !audioRef.current || !pointerRef.current)
        return;
      const container = containerRef.current;
      const audio = audioRef.current;
      const pointer = pointerRef.current;
      const containerRect = container.getBoundingClientRect();
      const maxX = containerRect.width;
      const currentProgress = audio.currentTime / audio.duration;
      const timeRemaining = (audio.duration - audio.currentTime) * 1000;
      const isRtl = lang === "ar";

      if (isRtl) {
        pointer.style.right = `${maxX * currentProgress - 5}px`;
        pointer.style.left = "auto";
        pointer.style.transition = "opacity 300ms ease-out";

        if (!audio.paused) {
          setTimeout(() => {
            pointer.style.right = `${maxX - 5}px`;
            pointer.style.transition = `right ${timeRemaining}ms linear, opacity 300ms ease-out`;
          }, 1);
        }
      } else {
        pointer.style.left = `${maxX * currentProgress - 5}px`;
        pointer.style.right = "auto";
        pointer.style.transition = "opacity 300ms ease-out";

        if (!audio.paused) {
          setTimeout(() => {
            pointer.style.left = `${maxX - 5}px`;
            pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
          }, 1);
        }
      }
      setPageWidth(window.innerWidth);
    };

    window.addEventListener("resize", handleWindowResize);
    return () => window.removeEventListener("resize", handleWindowResize);
  }, [lang, containerRef, pointerRef, setPageWidth]);

  // Apply language-based direction to the progress container
  useEffect(() => {
    if (!containerRef.current) return;

    const container = containerRef.current;
    container.style.direction = lang === "ar" ? "rtl" : "ltr";
  }, [lang, containerRef]);

  // Handle language change while audio is playing
  useEffect(() => {
    if (
      !progressRef.current ||
      !pointerRef.current ||
      !audioRef.current ||
      !containerRef.current ||
      !audioState
    )
      return;

    const progress = progressRef.current;
    const audio = audioRef.current;
    const pointer = pointerRef.current;
    const container = containerRef.current;
    const isRtl = lang === "ar";

    // Reset transitions
    pointer.style.transition = "none";
    progress.style.transition = "none";

    const currentProgress = audio.currentTime / audio.duration;
    const containerRect = container.getBoundingClientRect();
    const maxX = containerRect.width;

    // Update pointer position with the new direction
    if (isRtl) {
      pointer.style.right = `${maxX * currentProgress - 5}px`;
      pointer.style.left = "auto";
    } else {
      pointer.style.left = `${maxX * currentProgress - 5}px`;
      pointer.style.right = "auto";
    }

    // Update progress bar with current progress
    progress.style.width = `${currentProgress * 100}%`;

    // If audio is playing, we need to restore the animation
    if (!audio.paused && audioState.playing) {
      const timeRemaining = (audio.duration - audio.currentTime) * 1000;

      // Short delay to apply the transition after the position update
      setTimeout(() => {
        progress.style.width = "100%";
        progress.style.transition = `width ${timeRemaining}ms linear`;

        if (isRtl) {
          pointer.style.right = `${maxX - 5}px`;
          pointer.style.transition = `right ${timeRemaining}ms linear, opacity 300ms ease-out`;
        } else {
          pointer.style.left = `${maxX - 5}px`;
          pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
        }
      }, 10);
    }
  }, [lang, audioState, containerRef, pointerRef, progressRef]);

  // Prevent loading state during language changes
  useEffect(() => {
    // When language changes, ensure loading state is cleared if audio is ready
    if (audioRef.current && audioRef.current.readyState >= 3) {
      // Use a small delay to ensure this runs after the track effect
      const timeoutId = setTimeout(() => {
        setIsLoading(false);
      }, 10);

      return () => clearTimeout(timeoutId);
    }
  }, [lang, setIsLoading]);

  // Removed automatic play button clicking to prevent loops

  // Set loading state only when track index changes (not language or other changes)
  useEffect(() => {
    if (!audioRef.current) return;

    // Only show loading when switching tracks while playing
    if (!audioRef.current.paused || playingStateRef.current) {
      setIsLoading(true);
    }
  }, [playing]); // Only depend on playing index, not playlist content

  // Add waiting and playing event handlers
  useEffect(() => {
    if (!audioRef.current) return;
    const audio = audioRef.current;
    let loadingTimeout: ReturnType<typeof setTimeout>;

    const handleWaiting = () => {
      if (loadingTimeout) clearTimeout(loadingTimeout);
      loadingTimeout = setTimeout(() => {
        if (!audio.paused && audio.readyState < 3) {
          setIsLoading(true);
        }
      }, 500);
    };

    const handlePlaying = () => {
      if (loadingTimeout) clearTimeout(loadingTimeout);
      setIsLoading(false);
    };

    const handleLoadStart = () => {
      if (loadingTimeout) clearTimeout(loadingTimeout);
      if (!audio.paused || playingStateRef.current) {
        setIsLoading(true);
      }
    };

    const handleCanPlay = () => {
      if (loadingTimeout) clearTimeout(loadingTimeout);
      setIsLoading(false);
    };

    const handlePause = () => {
      if (loadingTimeout) clearTimeout(loadingTimeout);
      // Only clear loading if we're not in the middle of loading
      if (audio.readyState >= 3) {
        setIsLoading(false);
      }
    };

    const handleError = () => {
      // Only show loading if we're trying to play and there's no network
      if (!navigator.onLine && (playingStateRef.current || !audio.paused)) {
        setIsLoading(true);
      } else {
        setIsLoading(false);
      }
    };

    // Handle network status changes
    const handleOnline = () => {
      if (audio.error || audio.readyState < 3) {
        audio.load();
        if (playingStateRef.current || !audio.paused) {
          setIsLoading(true);
          playAudio(audio);
        }
      }
    };

    const handleOffline = () => {
      // Keep showing loading if we're trying to play
      if (playingStateRef.current || !audio.paused) {
        setIsLoading(true);
      }
    };

    audio.addEventListener("waiting", handleWaiting);
    audio.addEventListener("playing", handlePlaying);
    audio.addEventListener("loadstart", handleLoadStart);
    audio.addEventListener("canplay", handleCanPlay);
    audio.addEventListener("pause", handlePause);
    audio.addEventListener("error", handleError);
    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    // Initial network check
    if (!navigator.onLine && (playingStateRef.current || !audio.paused)) {
      setIsLoading(true);
    }

    return () => {
      if (loadingTimeout) clearTimeout(loadingTimeout);
      audio.removeEventListener("waiting", handleWaiting);
      audio.removeEventListener("playing", handlePlaying);
      audio.removeEventListener("loadstart", handleLoadStart);
      audio.removeEventListener("canplay", handleCanPlay);
      audio.removeEventListener("pause", handlePause);
      audio.removeEventListener("error", handleError);
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, [setIsLoading, playingStateRef, playAudio]);

  return (
    <div ref={playerRef} className="player">
      <audio
        ref={audioRef}
        src={playlist[playing].src}
        onLoadedMetadata={onMetaDataLoad}
        muted={extensionMode}
        onError={() => {
          // Additional error handling for the audio element
          setIsLoading(false);
          if (navigator.onLine && audioRef.current) {
            audioRef.current.load();
          }
        }}
        onEnded={() => {
          if (
            !audioRef.current ||
            !pointerRef.current ||
            !progressRef.current ||
            !nextBtnRef.current
          )
            return;
          const pointer = pointerRef.current;
          const progress = progressRef.current;
          const audio = audioRef.current;
          const nextBtn = nextBtnRef.current;
          const isRtl = lang === "ar";

          if (loopStateRef.current) {
            if (!audioState) return;

            // Reset audio time
            audio.currentTime = 0;

            // Reset visual progress bar
            progress.style.width = "0";

            if (isRtl) {
              pointer.style.right = `-5px`;
              pointer.style.left = "auto";
            } else {
              pointer.style.left = `-5px`;
              pointer.style.right = "auto";
            }

            progress.style.transition = "none";
            pointer.style.transition = "none";

            // Update playOptions for Surah component sync
            setPlayOptions({
              playing: true,
              currentTime: 0,
              duration: audioState.duration,
            });

            // Restart playback
            playAudio(audio);
            setAudioState({
              ...audioState,
              playing: true,
            });
          } else {
            nextBtn.click();
            // Trigger debounced extra smooth scroll for automatic track change
            scrollToCurrentItem(SCROLL_DURATIONS.EXTRA_SMOOTH);
          }
        }}
      ></audio>
      <div className={`audio-content ${lang == "en" ? "en-font" : "ar-font"}`}>
        <p className="surah-name">{playlist[playing].name}</p>
        <p className="qari-name">{playlist[playing].writer}</p>
      </div>
      <div className="progress">
        <div className="timestamp en-font">
          {audioRef.current && audioRef.current.duration ? (
            <p>
              <span className="start-timestamp">
                {(() => {
                  const currentTime = dayjs.duration(
                    audioRef.current.currentTime,
                    "seconds"
                  );
                  return currentTime.format("HH:mm:ss");
                })()}
              </span>
              <span> / </span>
              <span className="end-timestamp">
                {" "}
                {(() => {
                  const duration = dayjs.duration(
                    audioRef.current.duration,
                    "seconds"
                  );
                  return duration.format("HH:mm:ss");
                })()}
              </span>
            </p>
          ) : null}
        </div>
        <div
          ref={containerRef}
          onClick={onMouseClick}
          style={{
            cursor:
              audioState && audioRef.current?.duration ? "pointer" : "default",
            opacity: audioState && audioRef.current?.duration ? 1 : 0.5,
          }}
          className={`bar-container ${lang === "ar" ? "rtl" : "ltr"}`}
        >
          <div
            ref={pointerRef}
            onMouseDown={() => {
              if (audioState && audioRef.current?.duration) {
                wasPlayingBeforeDragRef.current = audioState.playing;
                setIsDragging(true);

                if (audioState.playing) {
                  // Pause the audio directly without calling pauseAudio to avoid side effects
                  audioRef.current.pause();

                  setAudioState((prev) =>
                    prev ? { ...prev, playing: false } : null
                  );
                }
              }
            }}
            onMouseUp={() => {
              if (audioState && audioRef.current?.duration) {
                // Let the window mouseUp handler deal with the resume logic
                // This prevents double handling when releasing over the pointer
              }
            }}
            style={{
              display:
                audioState && audioRef.current?.duration ? "block" : "none",
            }}
            className="pointer"
          ></div>
          <div ref={progressRef} className="progress-bar"></div>
        </div>
      </div>
      <div className="controls">
        <button
          onClick={() => {
            const stored = localStorage.getItem(storageKey);
            const storedData = stored ? JSON.parse(stored) : {};
            localStorage.setItem(
              storageKey,
              JSON.stringify({
                ...storedData,
                loop: !loopStateRef.current,
              })
            );
            setLoop(!loopStateRef.current);
            loopStateRef.current = !loopStateRef.current;
          }}
          className="loop-button"
        >
          {loop ? Icons.loop_btn : Icons.noloop_btn}
        </button>
        <div
          className="volume-control"
          onMouseEnter={() => {
            if (volumePanelTimeout.current) {
              clearTimeout(volumePanelTimeout.current);
            }
            setHoverVolume(true);
          }}
          onMouseLeave={() => {
            if (volumePanelTimeout.current) {
              clearTimeout(volumePanelTimeout.current);
            }
            volumePanelTimeout.current = setTimeout(
              () => setHoverVolume(false),
              300
            );
          }}
        >
          <button
            className="volume-button"
            onClick={() => setAudioVolume(audioVolume !== 0 ? 0 : 60)}
          >
            {audioVolume == 0
              ? Icons.muted_btn
              : audioVolume <= 50
              ? Icons.midvolume_btn
              : Icons.highvolume_btn}
          </button>

          <div
            style={{
              opacity: hoverVolume ? 1 : 0,
              visibility: hoverVolume ? "visible" : "hidden",
              transition: hoverVolume
                ? "opacity 300ms ease-in-out" // Immediate transition when showing
                : "opacity 300ms ease-in-out, visibility 0s 300ms", // Delayed hiding
            }}
            className="volume-panel-wrapper"
          >
            <Slider
              orientation="vertical"
              sx={() => ({
                color: "#686868",
              })}
              valueLabelDisplay="off"
              value={audioVolume}
              onChange={(_, newVolume) => {
                setAudioVolume(newVolume as number);
              }}
            />
          </div>
        </div>
        <div className="progress-btns">
          <button
            onClick={() => {
              if (playing === 0) {
                const stored = localStorage.getItem(storageKey);
                const storedData = stored ? JSON.parse(stored) : {};
                localStorage.setItem(
                  storageKey,
                  JSON.stringify({
                    ...storedData,
                    playing: playlist.length - 1,
                    currentTime: 0,
                  })
                );

                setPlaying(playlist.length - 1);
              } else {
                const stored = localStorage.getItem(storageKey);
                const extensionData = stored ? JSON.parse(stored) : {};
                localStorage.setItem(
                  storageKey,
                  JSON.stringify({
                    ...extensionData,
                    playing: playing - 1,
                    currentTime: 0,
                  })
                );

                setPlaying(playing - 1);
              }
              // Trigger debounced extra smooth scroll for better UX
              scrollToCurrentItem(SCROLL_DURATIONS.EXTRA_SMOOTH);
            }}
            className={`prev-button ${lang == "ar" ? "flipped" : ""}`}
          >
            {Icons.prev_btn}
          </button>
          <button
            ref={playBtnRef}
            onClick={(e) => {
              e.preventDefault();
              if (isLoading) return;

              if (!audioRef.current || !audioState) return;
              const audio = audioRef.current;

              if (audioState.playing) {
                pauseAudio(audio);
                setAudioState((prev) =>
                  prev ? { ...prev, playing: false } : null
                );
              } else {
                playAudio(audio);
                setAudioState((prev) =>
                  prev ? { ...prev, playing: true } : null
                );
              }
            }}
            className="play-button"
            style={{ pointerEvents: isLoading ? "none" : "auto" }}
          >
            {isLoading ? (
              <div className="spinner" />
            ) : audioState?.playing ? (
              Icons.pause_btn
            ) : (
              Icons.play_btn
            )}
          </button>
          <button
            onClick={() => {
              if (playing === playlist.length - 1) {
                const stored = localStorage.getItem(storageKey);
                const storedData = stored ? JSON.parse(stored) : {};
                localStorage.setItem(
                  storageKey,
                  JSON.stringify({
                    ...storedData,
                    playing: 0,
                    currentTime: 0,
                  })
                );

                setPlaying(0);
              } else {
                const stored = localStorage.getItem(storageKey);
                const storedData = stored ? JSON.parse(stored) : {};
                localStorage.setItem(
                  storageKey,
                  JSON.stringify({
                    ...storedData,
                    playing: playing + 1,
                    currentTime: 0,
                  })
                );

                setPlaying(playing + 1);
              }
              // Trigger debounced extra smooth scroll for better UX
              scrollToCurrentItem(SCROLL_DURATIONS.EXTRA_SMOOTH);
            }}
            ref={nextBtnRef}
            className={`next-button ${lang == "ar" ? "flipped" : ""}`}
          >
            {Icons.next_btn}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Player;
