import { GlobalStates } from "../GlobalStates";
import "../styles/components/Player.scss";
import { useRef, useEffect, useContext, useState, useCallback } from "react";
import { GlobalStatesContext } from "../types";
import dayjs from "dayjs";
import Slider from "@mui/material/Slider";
import duration from "dayjs/plugin/duration";

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
  const [audioVolume, setAudioVolume] = useState(audioVolumeRef.current);
  const [loop, setLoop] = useState<boolean>(loopStateRef.current);
  const { playlist, playing, setPlaying } =
    useContext<GlobalStatesContext>(GlobalStates);
  const playBtnTimeout = useRef<number | null>(null);
  const volumePanelTimeout = useRef<number | null>(null);
  const intervalRef = useRef<number | null>(null);
  const [now, setNow] = useState<number>(0);
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

    const timeRemaining = (audioState.duration - audio.currentTime) * 1000;
    const currentProgress = audio.currentTime / audioState.duration;
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
  useEffect(() => {
    if (!pointerRef.current || !progressRef.current) return;
    const pointer = pointerRef.current;
    const progress = progressRef.current;
    progress.style.width = "0";
    pointer.style.left = `-5px`;
    progress.style.transition = "none";
    pointer.style.transition = "none";
  }, [playing]);
  useEffect(() => {
    if (!audioRef.current) return;
    const audio = audioRef.current;
    audioVolumeRef.current = audioVolume;
    audio.volume = audioVolume / 100;
  }, [audioVolume]);
  return (
    <div ref={playerRef} className="player">
      <audio
        ref={audioRef}
        src={playlist[playing - 1].src}
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
        <p className="surah-name">{playlist[playing - 1].name}</p>
        <p className="qari-name">{playlist[playing - 1].writer}</p>
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
          {loop ? (
            <svg
              stroke="currentColor"
              fill="none"
              strokeWidth="2"
              viewBox="0 0 24 24"
              strokeLinecap="round"
              strokeLinejoin="round"
              height="1em"
              width="1em"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M4 12v-3a3 3 0 0 1 3 -3h13m-3 -3l3 3l-3 3"></path>
              <path d="M20 12v3a3 3 0 0 1 -3 3h-13m3 3l-3 -3l3 -3"></path>
            </svg>
          ) : (
            <svg
              stroke="currentColor"
              fill="none"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke-linecap="round"
              stroke-linejoin="round"
              height="1em"
              width="1em"
              xmlns="http://www.w3.org/2000/svg"
            >
              <desc></desc>
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M4 12v-3c0 -1.336 .873 -2.468 2.08 -2.856m3.92 -.144h10m-3 -3l3 3l-3 3"></path>
              <path d="M20 12v3a3 3 0 0 1 -.133 .886m-1.99 1.984a3 3 0 0 1 -.877 .13h-13m3 3l-3 -3l3 -3"></path>
              <path d="M3 3l18 18"></path>
            </svg>
          )}
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
          {audioVolume == 0 ? (
            <svg
              stroke="currentColor"
              fill="none"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke-linecap="round"
              stroke-linejoin="round"
              height="100%"
              width="100%"
              xmlns="http://www.w3.org/2000/svg"
            >
              <desc></desc>
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M6 15h-2a1 1 0 0 1 -1 -1v-4a1 1 0 0 1 1 -1h2l3.5 -4.5a0.8 .8 0 0 1 1.5 .5v14a0.8 .8 0 0 1 -1.5 .5l-3.5 -4.5"></path>
              <path d="M16 10l4 4m0 -4l-4 4"></path>
            </svg>
          ) : audioVolume <= 50 ? (
            <svg
              stroke="currentColor"
              fill="none"
              stroke-width="2"
              viewBox="0 0 24 24"
              stroke-linecap="round"
              stroke-linejoin="round"
              height="100%"
              width="100%"
              xmlns="http://www.w3.org/2000/svg"
            >
              <desc></desc>
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M15 8a5 5 0 0 1 0 8"></path>
              <path d="M6 15h-2a1 1 0 0 1 -1 -1v-4a1 1 0 0 1 1 -1h2l3.5 -4.5a0.8 .8 0 0 1 1.5 .5v14a0.8 .8 0 0 1 -1.5 .5l-3.5 -4.5"></path>
            </svg>
          ) : (
            <svg
              stroke="currentColor"
              fill="none"
              strokeWidth="2"
              viewBox="0 0 24 24"
              strokeLinecap="round"
              strokeLinejoin="round"
              height="100%"
              width="100%"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
              <path d="M15 8a5 5 0 0 1 0 8"></path>
              <path d="M17.7 5a9 9 0 0 1 0 14"></path>
              <path d="M6 15h-2a1 1 0 0 1 -1 -1v-4a1 1 0 0 1 1 -1h2l3.5 -4.5a0.8 .8 0 0 1 1.5 .5v14a0.8 .8 0 0 1 -1.5 .5l-3.5 -4.5"></path>
            </svg>
          )}
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
            onChange={(e) => {
              setAudioVolume(e.target.value);
            }}
          />
        </div>
        <button
          onClick={() => {
            if (playing === 1) {
              setPlaying(114);
            } else {
              setPlaying(playing - 1);
            }
          }}
          className="prev-button"
        >
          <svg
            stroke="currentColor"
            fill="currentColor"
            strokeWidth="0"
            version="1.1"
            viewBox="0 0 16 16"
            height="1em"
            width="1em"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M8 0c-4.418 0-8 3.582-8 8s3.582 8 8 8 8-3.582 8-8-3.582-8-8-8zM8 14.5c-3.59 0-6.5-2.91-6.5-6.5s2.91-6.5 6.5-6.5 6.5 2.91 6.5 6.5-2.91 6.5-6.5 6.5z"></path>
            <path d="M7 8l4-3v6z"></path>
            <path d="M5 5h2v6h-2v-6z"></path>
          </svg>
        </button>
        <button
          ref={playBtnRef}
          onClick={handlePlayAudio}
          className="play-button"
        >
          {audioState?.playing ? (
            <svg
              stroke="currentColor"
              fill="currentColor"
              stroke-width="0"
              viewBox="0 0 24 24"
              height="1em"
              width="1em"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path fill="none" d="M0 0h24v24H0z"></path>
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 14H9V8h2v8zm4 0h-2V8h2v8z"></path>
            </svg>
          ) : (
            <svg
              stroke="currentColor"
              fill="currentColor"
              strokeWidth="0"
              viewBox="0 0 24 24"
              height="1em"
              width="1em"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path fill="none" d="M0 0h24v24H0z"></path>
              <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"></path>
            </svg>
          )}
        </button>
        <button
          onClick={() => {
            if (playing === 114) {
              setPlaying(1);
            } else {
              setPlaying(playing + 1);
            }
          }}
          ref={nextBtnRef}
          className="next-button"
        >
          <svg
            stroke="currentColor"
            fill="currentColor"
            strokeWidth="0"
            version="1.1"
            viewBox="0 0 16 16"
            height="1em"
            width="1em"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M8 0c4.418 0 8 3.582 8 8s-3.582 8-8 8-8-3.582-8-8 3.582-8 8-8zM8 14.5c3.59 0 6.5-2.91 6.5-6.5s-2.91-6.5-6.5-6.5-6.5 2.91-6.5 6.5 2.91 6.5 6.5 6.5z"></path>
            <path d="M9 8l-4-3v6z"></path>
            <path d="M11 5h-2v6h2v-6z"></path>
          </svg>
        </button>
      </div>
    </div>
  );
};

export default Player;
