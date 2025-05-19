import { SurahData } from "../types";
import "../styles/components/Surah.scss";
import { useContext, useEffect, useState, useRef } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext } from "../types";
import dayjs from "dayjs";
import duration from "dayjs/plugin/duration";
import { Icons } from "./Icons";

dayjs.extend(duration);

const Surah = ({ id, name }: SurahData) => {
  const {
    playing,
    playlist,
    lang,
    playOptions,
    setPlayOptions,
    qari,
    setSearchResult,
  } = useContext<GlobalStatesContext>(GlobalStates);
  const { setPlaying, extensionMode } =
    useContext<GlobalStatesContext>(GlobalStates);
  const onClick = () => {
    const surahPlaying = playlist.findIndex(({ id: surahId }) => surahId == id);
    setPlaying(surahPlaying);
    if (extensionMode) {
      const stored = localStorage.getItem("quranstream-extension");
      const extensionData = stored ? JSON.parse(stored) : {};
      localStorage.setItem(
        "quranstream-extension",
        JSON.stringify({
          ...extensionData,
          playing: surahPlaying,
        })
      );
    }
    setSearchResult("");
  };
  const [hovered, setHovered] = useState(false);
  const surahIndex = playlist.findIndex(({ id: surahId }) => surahId == id);
  const progressBarRef = useRef(null);

  useEffect(() => {
    if (progressBarRef.current && playOptions.duration) {
      const progressBar: HTMLElement = progressBarRef.current;
      const progress = (playOptions.currentTime / playOptions.duration) * 100;

      // Set initial position without transition
      progressBar.style.transition = "none";
      progressBar.style.width = `${progress}%`;

      // Apply transition if playing
      if (playOptions.playing) {
        const timeRemaining =
          (playOptions.duration - playOptions.currentTime) * 1000;
        setTimeout(() => {
          progressBar.style.transition = `width ${timeRemaining}ms linear`;
        }, 1);
        setTimeout(() => {
          progressBar.style.width = "100%";
        }, 1);
      }
    }
  }, [
    playOptions.currentTime,
    playOptions.duration,
    playOptions.playing,
    qari,
  ]);
  return (
    <>
      <div
        style={
          playing == surahIndex
            ? { backgroundColor: "#1DB954" }
            : hovered
            ? { backgroundColor: "#1DB954", opacity: 0.8 }
            : {}
        }
        onClick={onClick}
        className="surah-box"
        onMouseEnter={() => setHovered(true)}
        onMouseLeave={() => setHovered(false)}
      >
        <div className="id-box en-font">
          {playing == surahIndex ? (
            playOptions?.playing ? (
              <button
                onClick={() =>
                  setPlayOptions({ ...playOptions, playing: false })
                }
                className="icon-btn"
              >
                {Icons.pause_btn}
              </button>
            ) : (
              <button
                onClick={() =>
                  setPlayOptions({ ...playOptions, playing: true })
                }
                className="icon-btn"
              >
                {Icons.play_btn}
              </button>
            )
          ) : hovered ? (
            <button
              onClick={() => setPlayOptions({ ...playOptions, playing: true })}
              className="icon-btn"
            >
              {Icons.play_btn}
            </button>
          ) : (
            id
          )}
        </div>
        <div className={`${lang == "en" ? "en-font" : "ar-font"}`}>
          {name[lang as keyof typeof name]}
        </div>

        {playing == surahIndex ? (
          <div className="en-font">
            <span className="start-timestamp">
              {" "}
              {(() => {
                const currentTime = dayjs.duration(
                  playOptions.currentTime,
                  "seconds"
                );
                return currentTime.format("HH:mm:ss");
              })()}
            </span>{" "}
            /{" "}
            {(() => {
              const duration = dayjs.duration(playOptions.duration, "seconds");
              return playOptions.duration
                ? duration.format("HH:mm:ss")
                : "00:00:00";
            })()}
          </div>
        ) : null}
      </div>
      {playing == surahIndex ? (
        <div ref={progressBarRef} className="surah-progress-bar"></div>
      ) : (
        <hr />
      )}
    </>
  );
};
export default Surah;
