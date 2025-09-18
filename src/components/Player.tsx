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
  const volumePanelTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [, setNow] = useState<number>(0);
  const [isDragging, setIsDragging] = useState<boolean>(false);
  const [isPotentialDrag, setIsPotentialDrag] = useState<boolean>(false);
  const isDraggingRef = useRef<boolean>(false);
  const wasPlayingBeforeDragRef = useRef<boolean>(false);
  const dragStartPositionRef = useRef<{ x: number; y: number } | null>(null);
  const hasDraggedRef = useRef<boolean>(false);

  const [hoverVolume, setHoverVolume] = useState<boolean>(false);
  const componentLoadedRef = useRef<boolean>(false);
  const audioInitializedRef = useRef<boolean>(
    "paused" in storedData && !storedData.paused ? false : true
  );
  const previousLangRef = useRef<string>(lang);
  const previousAudioStateRef = useRef<{
    playing: boolean;
    duration: number;
  } | null>(null);
  const lastDragEndTime = useRef<number>(0);
  const lastCanPlayTime = useRef<number>(0);
  const lastPlayingTime = useRef<number>(0);
  const lastPlayOptionsSyncTime = useRef<number>(0);
  const lastProgressBarClickTime = useRef<number>(0);
  const previousPlayOptionsPlaying = useRef<boolean | undefined>(undefined);
  const cleanupInProgress = useRef<boolean>(false);
  const saveData = useCallback(
    (audio: HTMLAudioElement) => {
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
    },
    [storageKey]
  );
  const playAudio = useCallback(
    (audio: HTMLAudioElement) => {
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
    },
    [extensionMode, saveData]
  );
  const pauseAudio = useCallback(
    (audio: HTMLAudioElement) => {
      audio.pause();
      saveData(audio);
      if (extensionMode) {
        chrome.runtime.sendMessage({ type: "PAUSE_AUDIO" });
      }
    },
    [extensionMode, saveData]
  );

  const onMouseEnterVolume = () => {
    if (volumePanelTimeout.current) {
      clearTimeout(volumePanelTimeout.current);
    }
    setHoverVolume(true);
  };

  const onMouseLeaveVolume = () => {
    if (volumePanelTimeout.current) {
      clearTimeout(volumePanelTimeout.current);
    }
    volumePanelTimeout.current = setTimeout(() => setHoverVolume(false), 300);
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
      progress.style.transition = "none";
      pointer.style.transition = "none";
      positionPointer(pointer, -5, isRtl);

      // Force a reflow to ensure the reset takes effect
      void progress.offsetHeight;

      // After a small delay, start the progress bar animation for initial load
      setTimeout(() => {
        if (audio.duration && !audio.paused && containerRef.current) {
          const timeRemaining = (audio.duration - audio.currentTime) * 1000;
          const containerRect = containerRef.current.getBoundingClientRect();
          const maxX = containerRect.width;

          progress.style.width = "100%";
          progress.style.transition = `width ${timeRemaining}ms linear`;

          if (isRtl) {
            pointer.style.right = `${maxX - 5}px`;
            pointer.style.transition = `right ${timeRemaining}ms linear, opacity 300ms ease-out`;
          } else {
            pointer.style.left = `${maxX - 5}px`;
            pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
          }
        }
      }, 150); // Longer delay to ensure audio is ready
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

  // Handle mouse move during drag
  const onMouseMove = useCallback(
    (e: MouseEvent) => {
      // Check if we should start dragging based on mouse movement threshold
      if (dragStartPositionRef.current && !isDraggingRef.current) {
        const deltaX = Math.abs(e.clientX - dragStartPositionRef.current.x);
        const deltaY = Math.abs(e.clientY - dragStartPositionRef.current.y);
        const dragThreshold = 5; // pixels

        if (deltaX > dragThreshold || deltaY > dragThreshold) {
          // Start dragging
          isDraggingRef.current = true;
          setIsDragging(true);
          hasDraggedRef.current = true;

          // CRITICAL: Pause audio immediately when dragging starts
          if (audioRef.current && !audioRef.current.paused) {
            pauseAudio(audioRef.current);
            if (audioState) {
              setAudioState({ ...audioState, playing: false });
            }
            // Update playingStateRef to reflect paused state
            playingStateRef.current = false;
          }
        }
      }

      if (
        !isDraggingRef.current ||
        !audioState ||
        !containerRef.current ||
        !pointerRef.current ||
        !progressRef.current ||
        !audioRef.current
      )
        return;

      const pointer = pointerRef.current;
      const container = containerRef.current;
      const progressBar = progressRef.current;
      const audio = audioRef.current;
      const { duration } = audioState;
      const containerRect = container.getBoundingClientRect();
      const maxX = containerRect.width;
      const minX = 0;
      const isRtl = lang === "ar";

      let moveX;
      if (isRtl) {
        moveX = containerRect.right - e.clientX;
      } else {
        moveX = e.clientX - containerRect.left;
      }

      const clickX = Math.max(minX, Math.min(maxX, moveX));
      const audioProgress = (clickX / maxX) * 100;

      // Update UI immediately during drag
      positionPointer(pointer, clickX - 5, isRtl);
      progressBar.style.width = `${audioProgress}%`;
      progressBar.style.transition = "none";
      pointer.style.transition = "none";

      // Update audio time without triggering play/pause cycles
      audio.currentTime = (duration * audioProgress) / 100;

      // Update playOptions to keep it synchronized during dragging
      setPlayOptions({
        playing: playingStateRef.current,
        currentTime: audio.currentTime,
        duration: audio.duration,
      });

      // Sync with extension audio if in extension mode
      if (extensionMode) {
        chrome.runtime.sendMessage({
          type: "SEEK_AUDIO",
          currentTime: audio.currentTime,
        });
      }

      saveData(audio);
    },
    [
      audioState,
      lang,
      positionPointer,
      extensionMode,
      setPlayOptions,
      saveData,
      pauseAudio,
      setAudioState,
    ]
  );

  // Handle mouse down on progress bar for smooth dragging
  const onProgressBarMouseDown = useCallback(
    (e: React.MouseEvent<HTMLDivElement>) => {
      // Debounce progress bar clicks to prevent rapid clicking issues
      const now = Date.now();
      const timeSinceLastClick = now - lastProgressBarClickTime.current;
      console.log(timeSinceLastClick);
      if (timeSinceLastClick < 300) {
        return;
      }
      console.log("Clicked On Progress Bar!");

      lastProgressBarClickTime.current = now;

      if (
        !audioState ||
        !audioRef.current?.duration ||
        !containerRef.current ||
        !pointerRef.current ||
        !progressRef.current ||
        isLoading
      )
        return;

      // Prevent interactions while audio is loading to avoid race conditions
      if (audioRef.current.readyState < 3) {
        return;
      }

      const container = containerRef.current;
      const pointer = pointerRef.current;
      const progressBar = progressRef.current;
      const audio = audioRef.current;
      const containerRect = container.getBoundingClientRect();
      const maxX = containerRect.width;
      const isRtl = lang === "ar";
      const { duration } = audioState;

      // Calculate mouse position and corresponding audio progress
      let clickX;
      if (isRtl) {
        clickX = containerRect.right - e.clientX;
      } else {
        clickX = e.clientX - containerRect.left;
      }

      const audioProgress = (clickX / maxX) * 100;
      const newCurrentTime = (duration * audioProgress) / 100;

      // CRITICAL: Store playing state BEFORE pausing audio
      dragStartPositionRef.current = { x: e.clientX, y: e.clientY };
      wasPlayingBeforeDragRef.current = audioState.playing && !audio.paused;
      hasDraggedRef.current = false;
      setIsPotentialDrag(true);

      // Immediately move pointer to mouse position for visual feedback
      positionPointer(pointer, clickX - 5, isRtl);
      progressBar.style.width = `${audioProgress}%`;

      // CRITICAL: Pause audio BEFORE changing currentTime to prevent fragments
      if (!audio.paused) {
        pauseAudio(audio);
        setAudioState({ ...audioState, playing: false });
        // Update playingStateRef to reflect paused state
        playingStateRef.current = false;
      }

      // Update audio time and playOptions immediately
      audio.currentTime = newCurrentTime;
      setPlayOptions({
        playing: playingStateRef.current,
        currentTime: audio.currentTime,
        duration: audio.duration,
      });

      // Sync with extension audio if in extension mode
      if (extensionMode) {
        chrome.runtime.sendMessage({
          type: "SEEK_AUDIO",
          currentTime: audio.currentTime,
        });
      }

      saveData(audio);

      // Prevent the click event from firing immediately
      e.preventDefault();
    },
    [
      audioState,
      lang,
      positionPointer,
      extensionMode,
      pauseAudio,
      setPlayOptions,
      saveData,
      isLoading,
    ]
  );

  // Handle mouse up to end dragging
  const onMouseUp = useCallback(
    (e?: MouseEvent) => {
      if (!audioRef.current) return;
      // Handle click if we haven't dragged
      if (dragStartPositionRef.current && !hasDraggedRef.current && e) {
        if (playBtnRef.current && wasPlayingBeforeDragRef.current) {
          // For progress bar clicks, resume if it was playing before
          // (position was already changed in onProgressBarMouseDown)
          setTimeout(() => {
            if (playBtnRef.current) {
              playBtnRef.current.click();
            }
          }, 50);
        }
        // If it wasn't playing before a progress bar click, just stay paused at the new position

        // Reset drag state
        dragStartPositionRef.current = null;
        hasDraggedRef.current = false;
        setIsPotentialDrag(false);
        return;
      }

      if (isDraggingRef.current) {
        isDraggingRef.current = false;
        setIsDragging(false);
        lastDragEndTime.current = Date.now();

        // Resume playback only if it was playing before the interaction started
        if (
          wasPlayingBeforeDragRef.current &&
          audioRef.current &&
          playBtnRef.current
        ) {
          setTimeout(() => {
            if (playBtnRef.current) {
              playBtnRef.current.click();

              // CRITICAL: Restart progress bar animation after resume
              setTimeout(() => {
                if (
                  audioRef.current &&
                  progressRef.current &&
                  pointerRef.current &&
                  containerRef.current
                ) {
                  const audio = audioRef.current;
                  const progress = progressRef.current;
                  const pointer = pointerRef.current;
                  const container = containerRef.current;
                  const isRtl = lang === "ar";

                  if (audio.duration && !audio.paused) {
                    const timeRemaining =
                      (audio.duration - audio.currentTime) * 1000;
                    const containerRect = container.getBoundingClientRect();
                    const maxX = containerRect.width;

                    // Restart the smooth animation
                    progress.style.transition = `width ${timeRemaining}ms linear`;
                    progress.style.width = "100%";

                    if (isRtl) {
                      pointer.style.right = `${maxX - 5}px`;
                      pointer.style.transition = `right ${timeRemaining}ms linear, opacity 300ms ease-out`;
                    } else {
                      pointer.style.left = `${maxX - 5}px`;
                      pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
                    }
                  }
                }
              }, 150); // Wait for audio to fully resume
            }
          }, 100); // Small delay to ensure drag state is cleared
        }

        // Restore transitions after drag ends
        if (progressRef.current && pointerRef.current) {
          setTimeout(() => {
            if (progressRef.current && pointerRef.current) {
              progressRef.current.style.transition = "width 100ms linear";
              pointerRef.current.style.transition = "opacity 300ms ease-out";
            }
          }, 50);
        }
      } else {
        // For non-drag interactions (simple clicks), also restore transitions
        if (progressRef.current && pointerRef.current) {
          setTimeout(() => {
            if (progressRef.current && pointerRef.current) {
              progressRef.current.style.transition = "width 100ms linear";
              pointerRef.current.style.transition = "opacity 300ms ease-out";
            }
          }, 50);
        }
      }

      // Reset drag state
      dragStartPositionRef.current = null;
      hasDraggedRef.current = false;
      setIsPotentialDrag(false);
      saveData(audioRef.current);
    },
    [saveData]
  );

  // Add/remove mouse event listeners for dragging
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => onMouseMove(e);
    const handleMouseUp = (e: MouseEvent) => onMouseUp(e);

    if (isDragging || isPotentialDrag) {
      window.addEventListener("mousemove", handleMouseMove);
      window.addEventListener("mouseup", handleMouseUp);
    }

    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
    };
  }, [isDragging, isPotentialDrag, onMouseMove, onMouseUp]);

  // Reset progress bar when switching tracks - consolidated effect
  useEffect(() => {
    if (
      !progressRef.current ||
      !pointerRef.current ||
      !audioRef.current ||
      !playBtnRef.current
    ) {
      return;
    }

    const progress = progressRef.current;
    const pointer = pointerRef.current;
    const playBtn = playBtnRef.current;
    const isRtl = lang === "ar";

    // Immediately reset progress and pointer without transition
    progress.style.transition = "none";
    pointer.style.transition = "none";
    progress.style.width = "0";
    positionPointer(pointer, -5, isRtl);

    // Force a reflow to ensure the "none" transition takes effect
    void progress.offsetHeight;

    // Auto-play if audio was playing (only if audioState is available)
    if (audioState && !audioState.playing) {
      playBtn.click();
    }
  }, [playing, qari, moshaf, lang, positionPointer]); // Consolidated dependencies

  // Update progress bar and pointer position
  useEffect(() => {
    const previousAudioState = previousAudioStateRef.current;
    const currentAudioState = audioState
      ? { playing: audioState.playing, duration: audioState.duration }
      : null;

    // Guard: Skip if dragging to prevent interference
    if (isDraggingRef.current) {
      return;
    }

    // Guard: Skip if recently finished dragging to prevent interference
    const timeSinceLastDrag = Date.now() - lastDragEndTime.current;
    if (timeSinceLastDrag < 300) {
      return;
    }

    // Guard: Skip if audioState hasn't meaningfully changed (but allow language changes)
    if (
      previousAudioState &&
      currentAudioState &&
      previousAudioState.playing === currentAudioState.playing &&
      previousAudioState.duration === currentAudioState.duration &&
      previousLangRef.current === lang
    ) {
      return;
    }

    // Update the previous state refs
    previousAudioStateRef.current = currentAudioState;

    if (
      !progressRef.current ||
      !pointerRef.current ||
      !audioRef.current ||
      !containerRef.current ||
      !audioState
    ) {
      return;
    }

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
      // Small delay to ensure any resets have completed first
      setTimeout(() => {
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
      }, 50); // 50ms delay to prevent race conditions
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
      // Guard: Prevent redundant cleanup calls
      if (cleanupInProgress.current) {
        return;
      }
      cleanupInProgress.current = true;

      progress.style.transition = "none";
      pointer.style.transition = "none";

      // Reset cleanup flag after a short delay
      setTimeout(() => {
        cleanupInProgress.current = false;
      }, 10);
    };
  }, [audioState, lang]);

  // REMOVED: Duplicate "Reset the Slider on new Surah" effect - consolidated into track change effect above
  useEffect(() => {
    if (
      !pointerRef.current ||
      !progressRef.current ||
      !audioState ||
      !playBtnRef.current ||
      !audioRef.current
    ) {
      return;
    }

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
    if (!audioRef.current) {
      return;
    }

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
      if (!containerRef.current || !audioRef.current || !pointerRef.current) {
        return;
      }

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

    return () => {
      window.removeEventListener("resize", handleWindowResize);
    };
  }, [lang]);

  // Apply language-based direction to the progress container
  useEffect(() => {
    if (!containerRef.current) {
      return;
    }

    const container = containerRef.current;
    const direction = lang === "ar" ? "rtl" : "ltr";
    container.style.direction = direction;
  }, [lang]);

  // Handle language change while audio is playing - ONLY when language actually changes
  useEffect(() => {
    const previousLang = previousLangRef.current;

    // Guard: Only proceed if language actually changed
    if (lang === previousLang) {
      return;
    }

    // Update the previous language ref
    previousLangRef.current = lang;

    if (
      !progressRef.current ||
      !pointerRef.current ||
      !audioRef.current ||
      !containerRef.current ||
      !audioState
    ) {
      return;
    }

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
  }, [lang]); // Removed audioState from dependencies - only trigger on actual language changes

  useEffect(() => {
    const currentPlaying = playOptions?.playing;
    const needsSync =
      audioRef.current &&
      playBtnRef.current &&
      audioRef.current.paused !== !currentPlaying;

    // Guard: Skip if currently dragging to prevent interference
    if (isDraggingRef.current) {
      return;
    }

    // Guard: Skip if play state hasn't actually changed
    if (previousPlayOptionsPlaying.current === currentPlaying) {
      return;
    }

    // Guard: Throttle rapid sync attempts
    const now = Date.now();
    if (now - lastPlayOptionsSyncTime.current < 150) {
      return;
    }

    previousPlayOptionsPlaying.current = currentPlaying;
    lastPlayOptionsSyncTime.current = now;

    if (needsSync) {
      playBtnRef.current.click();
    }
  }, [playOptions?.playing]);

  // Set loading state when src changes
  useEffect(() => {
    if (!audioRef.current) {
      return;
    }

    // Show loading immediately when switching tracks while playing
    if (!audioRef.current.paused || playingStateRef.current) {
      setIsLoading(true);
    }
  }, [playlist[playing].src]);

  // Add waiting and playing event handlers
  useEffect(() => {
    if (!audioRef.current) {
      return;
    }

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
      const now = Date.now();
      // Throttle playing events to prevent spam
      if (now - lastPlayingTime.current < 100) {
        return;
      }
      lastPlayingTime.current = now;

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
      // Skip if currently dragging to prevent interference
      if (isDraggingRef.current) {
        return;
      }

      const now = Date.now();
      // Throttle canplay events to prevent infinite spam
      if (now - lastCanPlayTime.current < 100) {
        return;
      }
      lastCanPlayTime.current = now;

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

            // Reset audio time and progress bar
            audio.currentTime = 0;
            progress.style.width = "0";
            progress.style.transition = "none";
            pointer.style.transition = "none";

            if (isRtl) {
              pointer.style.right = `-5px`;
              pointer.style.left = "auto";
            } else {
              pointer.style.left = `-5px`;
              pointer.style.right = "auto";
            }

            // Force a reflow to ensure the reset takes effect
            void progress.offsetHeight;

            // Start playing again
            playAudio(audio);

            // Update the playing state ref
            playingStateRef.current = true;

            // Start the interval for progress updates (like in handlePlayAudio)
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
                  JSON.stringify({
                    ...storedData,
                    currentTime: audio.currentTime,
                  })
                );
              }
            }, 1000);

            // Update the audio state to trigger the progress bar animation
            setAudioState({
              playing: true,
              duration: audioState.duration,
            });

            // Update playOptions to sync with the new state
            setPlayOptions({
              playing: true,
              currentTime: 0,
              duration: audio.duration,
            });

            // After a small delay, restart the progress bar animation
            setTimeout(() => {
              if (audio.duration && !audio.paused && containerRef.current) {
                const timeRemaining = audio.duration * 1000;
                const containerRect =
                  containerRef.current.getBoundingClientRect();
                const maxX = containerRect.width;

                progress.style.width = "100%";
                progress.style.transition = `width ${timeRemaining}ms linear`;

                if (isRtl) {
                  pointer.style.right = `${maxX - 5}px`;
                  pointer.style.transition = `right ${timeRemaining}ms linear, opacity 300ms ease-out`;
                } else {
                  pointer.style.left = `${maxX - 5}px`;
                  pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
                }
              }
            }, 100);
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
          onMouseDown={onProgressBarMouseDown}
          style={{
            cursor:
              audioState && audioRef.current?.duration ? "pointer" : "default",
            opacity: audioState && audioRef.current?.duration ? 1 : 0.5,
          }}
          className={`bar-container ${lang === "ar" ? "rtl" : "ltr"}`}
        >
          <div
            ref={pointerRef}
            style={{
              display:
                audioState && audioRef.current?.duration ? "block" : "none",
              pointerEvents: "none", // Disable all pointer interactions
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
        <div className="volume-box">
          <div
            onMouseEnter={hoverVolume ? onMouseEnterVolume : undefined}
            onMouseLeave={onMouseLeaveVolume}
            style={hoverVolume ? { opacity: 1, visibility: "initial" } : {}}
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
          <button
            onMouseEnter={onMouseEnterVolume}
            onMouseLeave={onMouseLeaveVolume}
            className="volume-button"
            onClick={() => setAudioVolume(audioVolume !== 0 ? 0 : 60)}
          >
            {audioVolume == 0
              ? Icons.muted_btn
              : audioVolume <= 50
              ? Icons.midvolume_btn
              : Icons.highvolume_btn}
          </button>
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
            className={lang == "ar" ? "mirror-btn" : ""}
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
            className={lang == "ar" ? "mirror-btn" : ""}
          >
            {Icons.next_btn}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Player;
