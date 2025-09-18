import "../styles/components/Header.scss";
import { MdPerson3 } from "react-icons/md";
import { FaBookOpen, FaHeadphonesAlt, FaStar, FaRegStar } from "react-icons/fa";
import { FiExternalLink } from "react-icons/fi";
import Tooltip from "@mui/material/Tooltip";
import { useContext, useState } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext, MoshafsType, Language } from "../types";
import recitersList from "../data/quranmp3/reciters.json";
import moshafsData from "../data/quranmp3/moshafs.json";
import { useAutoScroll } from "../hooks/useAutoScroll";
import { SCROLL_DURATIONS } from "../constants/scrollConfig";

const Header = () => {
  const {
    qari,
    setMoshaf,
    moshaf,
    lang,
    setLang,
    playlist,
    playing,
    setPlaying,
    setSearchResult,
    searchResult,
    chooseReciter,
    setChooseReciter,
    pageWidth,
    isScrolling,
    storageKey,
    setCleanedSearchResult,
    normalizeText,
    extensionMode,
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

  // Use the centralized auto-scroll hook
  const { scrollToCurrentItem, scrollToTop } = useAutoScroll({
    playlist,
    playing,
    pageWidth,
  });

  const tooltipStyle =
    lang === "en"
      ? {
          fontFamily: "'Ubuntu', sans-serif",
          direction: "ltr",
        }
      : {
          fontFamily: "'El Messiri', sans-serif",
          direction: "rtl",
        };
  const isArabic = (text: string): boolean => {
    // Arabic Unicode range: 0600–06FF, plus extended blocks
    return /[\u0600-\u06FF]/.test(text);
  };

  return (
    <div className="header-container">
      <div dir="" className="header-headline-container">
        {extensionMode ? (
          <Tooltip
            title={lang === "en" ? "Leave a Review" : "اترك تقييمًا"}
            slotProps={{ tooltip: { sx: tooltipStyle } }}
            arrow
          >
            <button
              style={lang === "en" ? { left: "0" } : { right: "0" }}
              className="icon-headline-btn"
              onClick={() =>
                window.open(
                  "https://chromewebstore.google.com/detail/jofpmocniekfifgfglfmocjljeidgcfo/reviews",
                  "_blank"
                )
              }
            >
              <FaRegStar className="star-icon empty" />
              <FaStar className="star-icon filled" />
            </button>
          </Tooltip>
        ) : (
          <Tooltip
            title={lang === "en" ? "Get the Extension" : "حمّل الإضافة"}
            slotProps={{ tooltip: { sx: tooltipStyle } }}
            arrow
          >
            <button
              style={lang === "en" ? { left: "0" } : { right: "0" }}
              className="icon-headline-btn"
              onClick={() =>
                window.open(
                  "https://chromewebstore.google.com/detail/jofpmocniekfifgfglfmocjljeidgcfo",
                  "_blank"
                )
              }
            >
              <FiExternalLink className="ext-icon" />
            </button>
          </Tooltip>
        )}

        <div>
          <p
            className="brand-name"
            onClick={() => {
              if (extensionMode) {
                window.open("https://quranstream.org/", "_blank");
              } else {
                window.location.reload();
              }
            }}
          >
            QuranStream
          </p>
        </div>

        <div
          className="lang-switch"
          style={lang === "en" ? { right: "0" } : { left: "0" }}
        >
          <p
            className={`${lang == "ar" ? "en-font" : "ar-font"}`}
            onClick={() => {
              const newLang = lang == "en" ? "ar" : "en";
              setLang(newLang);
              const stored = localStorage.getItem(storageKey);
              const storedData = stored ? JSON.parse(stored) : {};
              localStorage.setItem(
                storageKey,
                JSON.stringify({
                  ...storedData,
                  lang: newLang,
                })
              );
            }}
          >
            {lang == "en" ? "عربي" : "English"}
          </p>
        </div>
      </div>

      <div className="tools-container">
        {" "}
        <div className="search-container">
          <input
            autoFocus
            value={searchResult}
            onChange={(e) => {
              const value = e.target.value;
              setSearchResult(value);
              setCleanedSearchResult(normalizeText(value));
            }}
            type="text"
            // Input font depends on actual typed text
            className={`${isArabic(searchResult) ? "ar-font" : "en-font"} ${
              lang === "en" ? "placeholder-en-font" : "placeholder-ar-font"
            }`}
            placeholder={
              chooseReciter
                ? lang === "en"
                  ? "Search Reciter..."
                  : "ابحث عن قارئ..."
                : lang === "en"
                ? "Search Surah..."
                : "ابحث عن سورة..."
            }
          />
        </div>
        <div className="filter-container">
          {chooseReciter ? (
            <div className="filter-btn-container">
              <Tooltip
                title={
                  isScrolling
                    ? ""
                    : lang == "en"
                    ? "Change Surah"
                    : "غيّر السورة"
                }
                slotProps={{ tooltip: { sx: tooltipStyle } }}
                arrow
              >
                <button
                  className={`reciter-name  ${
                    lang == "en" ? "en-font" : "ar-font"
                  }`}
                  onClick={() => {
                    setChooseReciter(false);
                    setSearchResult("");
                    setCleanedSearchResult("");
                    scrollToCurrentItem(playing, SCROLL_DURATIONS.INSTANT);
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
              <div
                style={{ position: "relative" }}
                className="filter-btn-container"
              >
                <Tooltip
                  title={
                    isScrolling
                      ? ""
                      : lang == "en"
                      ? "Change Reciter"
                      : "غيّر القارئ"
                  }
                  slotProps={{ tooltip: { sx: tooltipStyle } }}
                  arrow
                >
                  <button
                    onClick={() => {
                      setChooseReciter(true);
                      setSearchResult("");
                      setCleanedSearchResult("");
                      scrollToTop();
                    }}
                    className={`${lang == "en" ? "en-font" : "ar-font"}`}
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
                  <Tooltip title={"Change Moshaf"} arrow>
                    <>
                      <button
                        className={`${lang == "en" ? "en-font" : "ar-font"}`}
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
                          {[...availableMoshafs]
                            .map((m, i) => ({ ...m, originalIndex: i })) // attach original index
                            .sort((a, b) => {
                              const popA =
                                moshafs[a.moshaf_id][a.moshaf_type]
                                  ?.popularity ?? 0;
                              const popB =
                                moshafs[b.moshaf_id][b.moshaf_type]
                                  ?.popularity ?? 0;
                              return popB - popA;
                            })
                            .map(
                              ({ moshaf_id, moshaf_type, originalIndex }) => {
                                return (
                                  <button
                                    className={`${
                                      lang == "en" ? "en-font" : "ar-font"
                                    }`}
                                    onClick={() => {
                                      if (originalIndex !== moshaf) {
                                        setMoshaf(originalIndex);
                                        const stored =
                                          localStorage.getItem(storageKey);
                                        const storedData = stored
                                          ? JSON.parse(stored)
                                          : {};
                                        localStorage.setItem(
                                          storageKey,
                                          JSON.stringify({
                                            ...storedData,
                                            moshaf: originalIndex,
                                            currentTime: 0,
                                            playing: 0,
                                          })
                                        );

                                        setPlaying(0);
                                      }
                                      setChangeMoshaf(false);
                                      clearTimeout(
                                        changeMoshafTimeout as number
                                      );
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
