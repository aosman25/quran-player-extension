import { GlobalStates } from "../GlobalStates";
import "../styles/components/Player.scss";
import { useRef, useEffect, useContext, useState, useCallback } from "react";
import { GlobalStatesContext } from "../types";
import dayjs from "dayjs";
import Slider from "@mui/material/Slider";
import duration from "dayjs/plugin/duration";
import { Icons } from "./Icons";

dayjs.extend(duration);
const Player = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const pointerRef = useRef<HTMLDivElement>(null);
  const progressRef = useRef<HTMLDivElement>(null);
  const playerRef = useRef<HTMLDivElement>(null);
  const playBtnRef = useRef<HTMLButtonElement>(null);
  const nextBtnRef = useRef<HTMLButtonElement>(null);
  const playingStateRef = useRef<boolean>(false);
  const loopStateRef = useRef<boolean>(false);
  const audioRef = useRef<HTMLAudioElement>(null);
  const audioVolumeRef = useRef<number>(60);
  const [audioState, setAudioState] = useState<{
    playing: boolean;
    duration: number;
  } | null>(null);
  const [audioVolume, setAudioVolume] = useState<number>(
    audioVolumeRef.current
  );
  const [loop, setLoop] = useState<boolean>(loopStateRef.current);
  const { playlist, playing, setPlaying } =
    useContext<GlobalStatesContext>(GlobalStates);
  const playBtnTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);
  const volumePanelTimeout = useRef<ReturnType<typeof setTimeout> | null>(null);
  const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [, setNow] = useState<number>(0);
  const [isDragging, setIsDragging] = useState<boolean>(false);
  const [hoverVolume, setHoverVolume] = useState<boolean>(false);

  // Handle metadata load
  const onMetaDataLoad = useCallback(() => {
    if (!audioRef.current || !progressRef.current || !pointerRef.current)
      return;
    const audio = audioRef.current;
    const progress = progressRef.current;
    const pointer = pointerRef.current;

    setAudioState({
      playing: playingStateRef.current,
      duration: audio.duration,
    });
    if (playingStateRef.current) {
      audio.play();
      progress.style.width = "0";
      pointer.style.left = `-5px`;
    } else {
      audio.pause();
    }
  }, []);

  // Handle play/pause audio
  const handlePlayAudio = useCallback(() => {
    if (!audioRef.current || !audioState) return;
    const audio = audioRef.current;
    if (audioState.playing) {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
      playingStateRef.current = false;
      audio.pause();
    } else {
      setNow((now) => now + 1);
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
      intervalRef.current = setInterval(() => {
        setNow((now) => now + 1);
      }, 1000);
      playingStateRef.current = true;
      audio.play();
    }
    setAudioState({ ...audioState, playing: !audioState.playing });
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
        !playBtnRef.current
      )
        return;

      const pointer = pointerRef.current;
      const container = containerRef.current;
      const progressBar = progressRef.current;
      const audio = audioRef.current;
      const playBtn = playBtnRef.current;
      const containerRect = container.getBoundingClientRect();
      const maxX = containerRect.width;

      const { duration } = audioState;
      const clickX = e.clientX - containerRect.left;
      const audioProgress = (clickX / maxX) * 100;
      pointer.style.left = `${clickX - 5}px`;
      progressBar.style.width = `${audioProgress}%`;
      progressBar.style.transition = "none";
      audio.pause();
      setAudioState({ ...audioState, playing: false });

      if (playBtnTimeout.current) {
        clearTimeout(playBtnTimeout.current);
      }
      playBtnTimeout.current = setTimeout(() => playBtn.click(), 300);
      audio.currentTime = (duration * audioProgress) / 100;
    },
    [audioState]
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

      const { duration } = audioState;
      const moveX = e.clientX - containerRect.left;
      const clickX = Math.max(minX, Math.min(maxX, moveX));
      const audioProgress = (clickX / maxX) * 100;
      pointer.style.left = `${clickX - 5}px`;
      progressBar.style.width = `${audioProgress}%`;
      progressBar.style.transition = "none";
      audio.pause();
      setAudioState({ ...audioState, playing: false });

      if (playBtnTimeout.current) {
        clearTimeout(playBtnTimeout.current);
      }
      playBtnTimeout.current = setTimeout(() => {
        setIsDragging(false);
        playBtn.click();
      }, 300);
      audio.currentTime = (duration * audioProgress) / 100;
    },
    [audioState, isDragging]
  );

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

    const timeRemaining = (audio.duration - audio.currentTime) * 1000;
    const currentProgress = audio.currentTime / audio.duration;
    const containerRect = container.getBoundingClientRect();
    const maxX = containerRect.width;

    if (audioState.playing) {
      progress.style.width = "100%";
      progress.style.transition = `width ${timeRemaining}ms linear`;
      pointer.style.left = `${maxX - 5}px`;
      pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
    } else {
      progress.style.width = `${currentProgress * 100}%`;
      progress.style.transition = "none";
      pointer.style.left = `${maxX * currentProgress - 5}px`;
      pointer.style.transition = "opacity 300ms ease-out";
    }

    // Cleanup
    return () => {
      progress.style.transition = "none";
    };
  }, [audioState]);

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
      !playBtnRef.current
    )
      return;
    const pointer = pointerRef.current;
    const progress = progressRef.current;
    const playBtn = playBtnRef.current;
    progress.style.width = "0";
    pointer.style.left = `-5px`;
    progress.style.transition = "none";
    pointer.style.transition = "none";
    if (!audioState.playing) {
      playBtn.click();
    }
  }, [playing]);

  // Change the volume on slider move
  useEffect(() => {
    if (!audioRef.current) return;
    const audio = audioRef.current;
    audioVolumeRef.current = audioVolume;
    audio.volume = audioVolume / 100;
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
      pointer.style.left = `${maxX * currentProgress - 5}px`;
      pointer.style.transition = "opacity 300ms ease-out";
      if (!audio.paused) {
        setTimeout(() => {
          pointer.style.left = `${maxX - 5}px`;
          pointer.style.transition = `left ${timeRemaining}ms linear, opacity 300ms ease-out`;
        }, 1);
      }
    };

    window.addEventListener("resize", handleWindowResize);
    return () => window.removeEventListener("resize", handleWindowResize);
  }, []);
  return (
    <div ref={playerRef} className="player">
      <audio
        ref={audioRef}
        src={playlist[playing].src}
        onLoadedMetadata={onMetaDataLoad}
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
          if (loopStateRef.current) {
            if (!audioState) return;
            audio.currentTime = 0;
            progress.style.width = "0";
            pointer.style.left = `-5px`;
            progress.style.transition = "none";
            pointer.style.transition = "none";
            audio.play();
            setAudioState({ ...audioState });
          } else {
            nextBtn.click();
          }
        }}
      ></audio>
      <div className="audio-content">
        <p className="surah-name">{playlist[playing].name}</p>
        <p className="qari-name">{playlist[playing].writer}</p>
      </div>
      <div className="progress">
        <div className="timestamp">
          <p>
            <span className="start-timestamp">
              {audioRef.current
                ? (() => {
                    const currentTime = dayjs.duration(
                      audioRef.current.currentTime,
                      "seconds"
                    );
                    const duration = dayjs.duration(
                      audioRef.current.duration,
                      "seconds"
                    );
                    return duration.hours() > 0
                      ? currentTime.format("HH:mm:ss")
                      : currentTime.format("mm:ss");
                  })()
                : "00:00"}
            </span>
            <span> / </span>
            <span className="end-timestamp">
              {" "}
              {audioRef.current
                ? (() => {
                    const duration = dayjs.duration(
                      audioRef.current.duration,
                      "seconds"
                    );
                    return duration.hours() > 0
                      ? duration.format("HH:mm:ss")
                      : duration.format("mm:ss");
                  })()
                : "00:00"}
            </span>
          </p>
        </div>
        <div
          ref={containerRef}
          onClick={onMouseClick}
          className="bar-container"
        >
          <div
            ref={pointerRef}
            onMouseDown={() => setIsDragging(true)}
            onMouseUp={() => setIsDragging(false)}
            className="pointer"
          ></div>
          <div ref={progressRef} className="progress-bar"></div>
        </div>
      </div>
      <div className="controls">
        <button
          onClick={() => {
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
            opacity: hoverVolume ? 1 : 0,
            visibility: hoverVolume ? "visible" : "hidden",
            animation: hoverVolume ? "growShrink 300ms ease-in-out" : "none",
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
            valueLabelDisplay="auto"
            value={audioVolume}
            onChange={(_, newVolume) => {
              setAudioVolume(newVolume as number);
            }}
          />
        </div>
        <button
          onClick={() => {
            if (playing === 0) {
              setPlaying(playlist.length - 1);
            } else {
              setPlaying(playing - 1);
            }
          }}
          className="prev-button"
        >
          {Icons.prev_btn}
        </button>
        <button
          ref={playBtnRef}
          onClick={handlePlayAudio}
          className="play-button"
        >
          {audioState?.playing ? Icons.pause_btn : Icons.play_btn}
        </button>
        <button
          onClick={() => {
            if (playing === playlist.length - 1) {
              setPlaying(0);
            } else {
              setPlaying(playing + 1);
            }
          }}
          ref={nextBtnRef}
          className="next-button"
        >
          {Icons.next_btn}
        </button>
      </div>
    </div>
  );
};

export default Player;
