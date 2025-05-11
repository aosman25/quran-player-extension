import "../styles/components/Header.scss";
import { MdPerson3 } from "react-icons/md";
import { GoHeart } from "react-icons/go";
import { GoHeartFill } from "react-icons/go";
import { FaBookOpen } from "react-icons/fa";
import { FaHeadphonesAlt } from "react-icons/fa";
import Tooltip from "@mui/material/Tooltip";
import { useContext, useEffect, useRef, useState } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext, MoshafsType, Language, Play } from "../types";
import recitersList from "../data/quranmp3/reciters.json";
import moshafsData from "../data/quranmp3/moshafs.json";
import { animateScroll as scroll, scroller } from "react-scroll";

const Header = () => {
  const {
    loved,
    setLoved,
    qari,
    setMoshaf,
    moshaf,
    lang,
    playlist,
    playing,
    setPlaying,
    setSearchResult,
    searchResult,
    chooseReciter,
    setChooseReciter,
  } = useContext<GlobalStatesContext>(GlobalStates);
  const [changeMoshaf, setChangeMoshaf] = useState<boolean>(false);
  const availableMoshafs = recitersList[
    String(qari) as keyof typeof recitersList
  ]["moshaf"].map(({ moshaf_id, moshaf_type }) => {
    return {
      moshaf_id,
      moshaf_type,
    };
  });
  const [changeMoshafTimeout, setChangeMoshafTimeout] = useState<null | number>(
    null
  );
  const moshafs: MoshafsType = moshafsData;
  const scrollOptions = {
    duration: 700,
    smooth: true,
  };
  const playlistRef = useRef<Play[]>(playlist);
  const playingRef = useRef<number>(playing);
  useEffect(() => {
    playlistRef.current = playlist;
    playingRef.current = playing;
  }, [playlist, playing]);
  return (
    <div className="header-container">
      <div className="tools-container">
        {" "}
        <div className="search-container">
          <input
            autoFocus
            value={searchResult}
            onChange={(e) => setSearchResult(e.target.value)}
            type="text"
            placeholder={
              chooseReciter ? "Search Reciter..." : "Search Surah..."
            }
          />
          {!chooseReciter ? (
            <button onClick={() => setLoved(!loved)} className="love-btn">
              {loved ? (
                <GoHeartFill size={23} color="#FF0000" />
              ) : (
                <GoHeart size={23} color="white" />
              )}
            </button>
          ) : null}
        </div>
        <div className="filter-container">
          {chooseReciter ? (
            <div className="filter-btn-container">
              <Tooltip title="Change Surah" arrow>
                <button
                  className="reciter-name"
                  onClick={() => {
                    setChooseReciter(false);
                    setSearchResult("");
                    setTimeout(() => {
                      scroller.scrollTo(
                        String(
                          String(playlistRef.current[playingRef.current]["id"])
                        ),
                        { ...scrollOptions, offset: -80 }
                      );
                    }, 100);
                  }}
                >
                  <FaHeadphonesAlt className="filter-icon" />

                  {playlist[playing]["name"] +
                    " | " +
                    (
                      recitersList[String(qari) as keyof typeof recitersList][
                        "name"
                      ] as Language
                    )[lang as keyof Language] +
                    " | " +
                    (String(availableMoshafs[moshaf]["moshaf_id"]) in moshafs
                      ? (
                          moshafs[
                            String(availableMoshafs[moshaf]["moshaf_id"])
                          ][availableMoshafs[moshaf]["moshaf_type"]][
                            "name"
                          ] as Language
                        )[lang as keyof Language]
                      : "")}
                </button>
              </Tooltip>
            </div>
          ) : (
            <>
              <div className="filter-btn-container">
                <Tooltip title="Change Reciter" arrow>
                  <button
                    onClick={() => {
                      setChooseReciter(true);
                      setSearchResult("");
                      scroll.scrollToTop(scrollOptions);
                    }}
                  >
                    <MdPerson3 className="filter-icon" />
                    {(
                      recitersList[String(qari) as keyof typeof recitersList][
                        "name"
                      ] as Language
                    )[lang as keyof Language] +
                      (availableMoshafs.length == 1
                        ? " | " +
                          (
                            moshafs[
                              String(availableMoshafs[moshaf]["moshaf_id"])
                            ][availableMoshafs[moshaf]["moshaf_type"]][
                              "name"
                            ] as Language
                          )[lang as keyof Language]
                        : "")}
                  </button>
                </Tooltip>
              </div>
              {availableMoshafs.length > 1 ? (
                <div className="filter-btn-container">
                  <Tooltip title={changeMoshaf ? "" : "Change Moshaf"} arrow>
                    <>
                      <button
                        onMouseLeave={() =>
                          setChangeMoshafTimeout(
                            setTimeout(() => setChangeMoshaf(false), 1000)
                          )
                        }
                        onClick={() => {
                          clearTimeout(changeMoshafTimeout as number);
                          setChangeMoshaf(!changeMoshaf);
                        }}
                      >
                        <FaBookOpen className="filter-icon" />
                        {String(availableMoshafs[moshaf]["moshaf_id"]) in
                        moshafs
                          ? (
                              moshafs[
                                String(availableMoshafs[moshaf]["moshaf_id"])
                              ][availableMoshafs[moshaf]["moshaf_type"]][
                                "name"
                              ] as Language
                            )[lang as keyof Language]
                          : null}
                      </button>
                      <div
                        style={
                          changeMoshaf
                            ? { opacity: 1 }
                            : { opacity: 0, display: "none" }
                        }
                        className="mohafs-main-container"
                      >
                        <div></div>
                        <div
                          onMouseOver={() =>
                            clearTimeout(changeMoshafTimeout as number)
                          }
                          onMouseLeave={() =>
                            setChangeMoshafTimeout(
                              setTimeout(() => setChangeMoshaf(false), 1000)
                            )
                          }
                          className="mohafs-container"
                        >
                          {availableMoshafs.map(
                            ({ moshaf_id, moshaf_type }, index) => {
                              return (
                                <button
                                  onClick={() => {
                                    if (index !== moshaf) {
                                      setMoshaf(index);
                                      setPlaying(0);
                                    }
                                    setChangeMoshaf(false);
                                    clearTimeout(changeMoshafTimeout as number);
                                  }}
                                >
                                  {
                                    (
                                      moshafs[moshaf_id][moshaf_type][
                                        "name"
                                      ] as Language
                                    )[lang as keyof Language]
                                  }
                                </button>
                              );
                            }
                          )}
                        </div>
                        <div></div>
                      </div>
                    </>
                  </Tooltip>
                </div>
              ) : null}
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default Header;
