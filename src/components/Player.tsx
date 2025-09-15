import { GlobalStates } from "../GlobalStates";
import "../styles/components/Player.scss";
import { useRef, useEffect, useContext, useState, useCallback } from "react";
import { GlobalStatesContext } from "../types";
import dayjs from "dayjs";
import Slider from "@mui/material/Slider";
import duration from "dayjs/plugin/duration";
import { Icons } from "./Icons";
import { useAutoScroll } from "../hooks/useAutoScroll";
import { SCROLL_DURATIONS } from "../constants/scrollConfig";

dayjs.extend(duration);
const Player = () => {
  const {
    lang,
    playlist,
    playing,
    setPlaying,
    playOptions,
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

  const stored = localStorage.getItem(storageKey);
  const storedData = stored ? JSON.parse(stored) : {};
  const containerRef = useRef<HTMLDivElement>(null);
  const pointerRef = useRef<HTMLDivElement>(null);
  const progressRef = useRef<HTMLDivElement>(null);
  // Add auto-scroll functionality for smooth navigation
  const { scrollToCurrentItem } = useAutoScroll({
    playlist,
    playing,
    pageWidth,
  });

  const playerRef = useRef<HTMLDivElement>(null);
  const playBtnRef = useRef<HTMLButtonElement>(null);
  const nextBtnRef = useRef<HTMLButtonElement>(null);
  const playingStateRef = useRef<boolean>(
    "paused" in storedData ? !storedData.paused : false
  );
  const loopStateRef = useRef<boolean>(
    "loop" in storedData ? storedData.loop : false
  );
  const audioRef = useRef<HTMLAudioElement>(null);
  const audioVolumeRef = useRef<number>(
    "volume" in storedData ? storedData.volume * 100 : 60
  );
  const [audioState, setAudioState] = useState<{
    playing: boolean;
    duration: number;
  } | null>(null);
  const [audioVolume, setAudioVolume] = useState<number>(
    audioVolumeRef.current
  );
  const [loop, setLoop] = useState<boolean>(loopStateRef.current);
  const playBtnTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);
  const volumePanelTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [, setNow] = useState<number>(0);
  const [isDragging, setIsDragging] = useState<boolean>(false);
  const [hoverVolume, setHoverVolume] = useState<boolean>(false);
  const componentLoadedRef = useRef<boolean>(false);
  const audioInitializedRef = useRef<boolean>(
    "paused" in storedData && !storedData.paused ? false : true
  );
  const saveData = (audio: HTMLAudioElement) => {
    const stored = localStorage.getItem(storageKey);
    const storedData = stored ? JSON.parse(stored) : {};
    localStorage.setItem(
      storageKey,
      JSON.stringify({
        ...storedData,
        paused: !playingStateRef.current,
        currentTime: audio.currentTime,
      })
    );
  };
  const playAudio = (audio: HTMLAudioElement) => {
    audio.play();
    saveData(audio);
    if (extensionMode) {
      if (audioInitializedRef.current) {
        chrome.runtime.sendMessage({
          type: "PLAY_AUDIO",
        });
      }
      audioInitializedRef.current = true;
    }
  };
  const pauseAudio = (audio: HTMLAudioElement) => {
    audio.pause();
    saveData(audio);
    if (extensionMode) {
      chrome.runtime.sendMessage({ type: "PAUSE_AUDIO" });
    }
  };

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

    if (!componentLoadedRef.current) {
      const stored = localStorage.getItem(storageKey);
      const storedData = stored ? JSON.parse(stored) : {};
      audio.currentTime =
        "currentTime" in storedData ? storedData.currentTime : 0;
      if (!storedData.paused) {
        intervalRef.current = setInterval(() => {
          setNow((now) => now + 1);
          setPlayOptions({
            playing: playingStateRef.current,
            currentTime: audio.currentTime,
            duration: audio.duration,
          });
          if (!extensionMode) {
            const stored = localStorage.getItem(storageKey);
            const storedData = stored ? JSON.parse(stored) : {};
            localStorage.setItem(
              storageKey,
              JSON.stringify({ ...storedData, currentTime: audio.currentTime })
            );
          }
        }, 1000);
      }
      componentLoadedRef.current = true;
    }
    const progress = progressRef.current;
    const pointer = pointerRef.current;
    const isRtl = lang === "ar";

    setAudioState({
      playing: playingStateRef.current,
      duration: audio.duration,
    });
    setPlayOptions({
      playing: playingStateRef.current,
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
  }, [lang, positionPointer, extensionMode]);

  // Handle play/pause audio
  const handlePlayAudio = useCallback(() => {
    if (!audioRef.current || !audioState) return;
    const audio = audioRef.current;
    if (audioState.playing) {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
      playingStateRef.current = false;
      pauseAudio(audio);
    } else {
      setNow((now) => now + 1);
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
      intervalRef.current = setInterval(() => {
        setNow((now) => now + 1);
        setPlayOptions({
          playing: playingStateRef.current,
          currentTime: audio.currentTime,
          duration: audio.duration,
        });
        if (!extensionMode) {
          const stored = localStorage.getItem(storageKey);
          const storedData = stored ? JSON.parse(stored) : {};
          localStorage.setItem(
            storageKey,
            JSON.stringify({ ...storedData, currentTime: audio.currentTime })
          );
        }
      }, 1000);
      playingStateRef.current = true;
      playAudio(audio);
    }

    setAudioState({ ...audioState, playing: playingStateRef.current });
    setPlayOptions({
      playing: !audioState.playing,
      currentTime: audio.currentTime,
      duration: audio.duration,
    });
  }, [audioState]);

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
      const playBtn = playBtnRef.current;
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

      // Set new audio time
      audio.currentTime = (duration * audioProgress) / 100;
      pauseAudio(audio);
      setAudioState({ ...audioState, playing: false });
      setPlayOptions({
        playing: false,
        currentTime: audio.currentTime,
        duration: audio.duration,
      });

      // Resume playback after a very short delay
      if (playBtnTimeout.current) {
        clearTimeout(playBtnTimeout.current);
      }
      playBtnTimeout.current = setTimeout(() => {
        playBtn.click();
        // Restore transitions after playback resumes
        pointer.style.transition = "opacity 300ms ease-out";
        progressBar.style.transition = "width 100ms linear";
      }, 50);
    },
    [audioState, lang, positionPointer]
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
      const playBtn = playBtnRef.current;
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
      pauseAudio(audio);
      setAudioState({ ...audioState, playing: false });
      setPlayOptions({
        playing: false,
        currentTime: audio.currentTime,
        duration: audio.duration,
      });

      if (playBtnTimeout.current) {
        clearTimeout(playBtnTimeout.current);
      }
      playBtnTimeout.current = setTimeout(() => {
        setIsDragging(false);
        playBtn.click();
      }, 300);
      audio.currentTime = (duration * audioProgress) / 100;
    },
    [audioState, isDragging, lang, positionPointer]
  );

  // Reset progress bar when switching tracks
  useEffect(() => {
    if (!progressRef.current || !pointerRef.current) return;
    const progress = progressRef.current;
    const pointer = pointerRef.current;
    const isRtl = lang === "ar";

    // Immediately reset progress and pointer without transition
    progress.style.transition = "none";
    pointer.style.transition = "none";
    progress.style.width = "0";
    positionPointer(pointer, -5, isRtl);

    // Force a reflow to ensure the "none" transition takes effect
    void progress.offsetHeight;
  }, [playlist[playing].src, lang, positionPointer]);

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

    const progress = progressRef.current;
    const audio = audioRef.current;
    const pointer = pointerRef.current;
    const container = containerRef.current;
    const isRtl = lang === "ar";

    // Only update if we have valid duration
    if (!audio.duration) {
      progress.style.width = "0";
      positionPointer(pointer, -5, isRtl);
      return;
    }

    const timeRemaining = (audio.duration - audio.currentTime) * 1000;
    const currentProgress = audio.currentTime / audio.duration;
    const containerRect = container.getBoundingClientRect();
    const maxX = containerRect.width;

    if (audioState.playing && !audio.paused && audio.readyState >= 3) {
      progress.style.width = "100%";
      progress.style.transition = `width ${timeRemaining}ms linear`;

      if (isRtl) {
        pointer.style.right = `${maxX - 5}px`;
        pointer.style.left = "auto";
        pointer.style.transition = `right ${timeRemaining}ms linear, opacity 300ms ease-out`;
      } else {
        pointer.style.left = `${maxX - 5}px`;
        pointer.style.right = "auto";
        pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
      }
    } else {
      progress.style.width = `${currentProgress * 100}%`;
      progress.style.transition = "none";

      if (isRtl) {
        pointer.style.right = `${maxX * currentProgress - 5}px`;
        pointer.style.left = "auto";
        pointer.style.transition = "opacity 300ms ease-out";
      } else {
        pointer.style.left = `${maxX * currentProgress - 5}px`;
        pointer.style.right = "auto";
        pointer.style.transition = "opacity 300ms ease-out";
      }
    }

    // Cleanup
    return () => {
      progress.style.transition = "none";
      pointer.style.transition = "none";
    };
  }, [audioState, lang]);

  // Add/remove mousemove event listener for dragging
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => onMouseMove(e);
    if (isDragging) {
      window.addEventListener("mousemove", handleMouseMove);
    }
    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
    };
  }, [isDragging, onMouseMove]);

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
    const playBtn = playBtnRef.current;
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
    saveData(audioRef.current);
    if (!audioState.playing) {
      playBtn.click();
    }
  }, [playing, qari, moshaf]);
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
  }, [lang]);

  // Change the volume on slider move
  useEffect(() => {
    if (!audioRef.current) return;
    const audio = audioRef.current;
    audioVolumeRef.current = audioVolume;
    audio.volume = audioVolume / 100;
    const stored = localStorage.getItem(storageKey);
    const storedData = stored ? JSON.parse(stored) : {};
    localStorage.setItem(
      storageKey,
      JSON.stringify({
        ...storedData,
        volume: audio.volume,
      })
    );
    if (extensionMode) {
      chrome.runtime.sendMessage({
        type: "CHANGE_VOLUME",
        volume: audio.volume,
      });
    }
  }, [audioVolume]);

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
  }, [lang]);

  // Apply language-based direction to the progress container
  useEffect(() => {
    if (!containerRef.current) return;

    const container = containerRef.current;
    container.style.direction = lang === "ar" ? "rtl" : "ltr";
  }, [lang]);

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
  }, [lang, audioState]);

  useEffect(() => {
    if (
      audioRef.current &&
      playBtnRef.current &&
      audioRef.current.paused !== !playOptions?.playing
    ) {
      playBtnRef.current.click();
    }
  }, [playOptions?.playing]);

  // Set loading state when src changes
  useEffect(() => {
    if (!audioRef.current) return;

    // Show loading immediately when switching tracks while playing
    if (!audioRef.current.paused || playingStateRef.current) {
      setIsLoading(true);
    }
  }, [playlist[playing].src]);

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
  }, [setIsLoading]);

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
            audio.currentTime = 0;
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
            playAudio(audio);
            setAudioState({ ...audioState });
          } else {
            nextBtn.click();
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
            onMouseDown={() =>
              audioState && audioRef.current?.duration && setIsDragging(true)
            }
            onMouseUp={() =>
              audioState && audioRef.current?.duration && setIsDragging(false)
            }
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
        <button
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
          style={{
            opacity: 1,
            visibility: hoverVolume ? "visible" : "hidden",
            animation: hoverVolume ? "growShrink 300ms ease-in-out" : "none",
            transition: hoverVolume
              ? "opacity 300ms ease-in-out" // Immediate transition when showing
              : "opacity 300ms ease-in-out, visibility 0s 300ms", // Delayed hiding
          }}
          className={`volume-panel-wrapper volume-panel-wrapper-${
            lang == "en" ? "ltr" : "rtl"
          }`}
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
                scrollToCurrentItem(
                  playlist.length - 1,
                  SCROLL_DURATIONS.EXTRA_SMOOTH
                );
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
                scrollToCurrentItem(playing - 1, SCROLL_DURATIONS.EXTRA_SMOOTH);
              }
              // Trigger debounced extra smooth scroll for better UX
            }}
            style={lang == "ar" ? { transform: "scaleX(-1)" } : {}}
            className="prev-button"
          >
            {Icons.prev_btn}
          </button>
          <button
            ref={playBtnRef}
            onClick={
              isLoading
                ? (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                  }
                : handlePlayAudio
            }
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
                scrollToCurrentItem(0, SCROLL_DURATIONS.EXTRA_SMOOTH);
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
                scrollToCurrentItem(playing + 1, SCROLL_DURATIONS.EXTRA_SMOOTH);
              }
              // Trigger debounced extra smooth scroll for better UX
            }}
            ref={nextBtnRef}
            style={lang == "ar" ? { transform: "scaleX(-1)" } : {}}
            className="next-button"
          >
            {Icons.next_btn}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Player;
