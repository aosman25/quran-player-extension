import "../styles/components/Player.scss";
import { useRef, useEffect } from "react";

const Player = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const pointerRef = useRef<HTMLDivElement>(null);
  const progressRef = useRef<HTMLDivElement>(null);
  const playerRef = useRef<HTMLDivElement>(null);
  const isDragging = useRef(false);
  const coords = useRef({ startX: 0, lastX: 0 });

  useEffect(() => {
    if (
      !containerRef.current ||
      !pointerRef.current ||
      !progressRef.current ||
      !playerRef.current
    )
      return;

    const pointer = pointerRef.current;
    const container = containerRef.current;
    const progressBar = progressRef.current;
    const player = playerRef.current;

    const containerRect = container.getBoundingClientRect();
    const minX = 0;
    const maxX = containerRect.width;

    const onMouseDown = (e: MouseEvent) => {
      isDragging.current = true;
      coords.current.startX = e.clientX - pointer.offsetLeft;
      player.addEventListener("mousemove", onMouseMove);
      player.addEventListener("mouseup", onMouseUp);
    };

    const onMouseMove = (e: MouseEvent) => {
      if (!isDragging.current) return;

      let nextX = e.clientX - coords.current.startX;
      nextX = Math.max(minX, Math.min(maxX, nextX)); // Constrain within bounds

      pointer.style.left = `${nextX - 5}px`;
      if (progressBar) {
        progressBar.style.width = `${(nextX / maxX) * 100}%`; // Update progress bar
      }
    };

    const onMouseUp = () => {
      isDragging.current = false;
      player.removeEventListener("mousemove", onMouseMove);
      player.removeEventListener("mouseup", onMouseUp);
    };

    const onMouseClick = (e: MouseEvent) => {
      if (isDragging.current) return;

      const clickX = e.clientX - container.offsetLeft;
      pointer.style.left = `${clickX - 5}px`;
      progressBar.style.width = `${(clickX / maxX) * 100}%`;
    };

    pointer.addEventListener("mousedown", onMouseDown);
    container.addEventListener("click", onMouseClick);

    return () => {
      pointer.removeEventListener("mousedown", onMouseDown);
      container.removeEventListener("click", onMouseClick);
    };
  }, []);
  return (
    <div ref={playerRef} className="player">
      <div className="audio-content">
        <p className="surah-name">Surat Al-Fatheh</p>
        <p className="qari-name">Mishari Elafassi</p>
      </div>
      <div className="progress">
        <div className="timestamp">
          <p>
            <span className="start-timestamp">00:00 </span>
            <span className="end-timestamp">/ 00:51</span>
          </p>
        </div>
        <div ref={containerRef} className="bar-container">
          <div ref={pointerRef} className="pointer"></div>
          <div ref={progressRef} className="progress-bar"></div>
        </div>
      </div>
      <div className="controls">
        <button className="loop-button">
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
            <path d="M4 12v-3a3 3 0 0 1 3 -3h13m-3 -3l3 3l-3 3"></path>
            <path d="M20 12v3a3 3 0 0 1 -3 3h-13m3 3l-3 -3l3 -3"></path>
          </svg>
        </button>
        <button className="volume-button">
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
            <path d="M17.7 5a9 9 0 0 1 0 14"></path>
            <path d="M6 15h-2a1 1 0 0 1 -1 -1v-4a1 1 0 0 1 1 -1h2l3.5 -4.5a0.8 .8 0 0 1 1.5 .5v14a0.8 .8 0 0 1 -1.5 .5l-3.5 -4.5"></path>
          </svg>
        </button>
        <button className="prev-button">
          <svg
            stroke="currentColor"
            fill="currentColor"
            stroke-width="0"
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
        <button className="play-button">
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
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 14.5v-9l6 4.5-6 4.5z"></path>
          </svg>
        </button>
        <button className="next-button">
          <svg
            stroke="currentColor"
            fill="currentColor"
            stroke-width="0"
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
