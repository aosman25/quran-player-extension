import Player from "./Player";
import Surah from "./Surah";
import { GlobalStatesContext, Play } from "../types";
import { useContext, useEffect, useRef } from "react";
import { GlobalStates } from "../GlobalStates";
import Header from "./Header";
import reciterNames from "../data/quranmp3/sorted_reciter_names.json";
import ReciterList from "./ReciterList";
import "../styles/components/Extension.scss";
import { Element, scroller } from "react-scroll";
import NotFound from "./NotFound";

type ReciterName = {
  id: number;
  name: string;
};

type ReciterNamesType = {
  ar: Record<string, ReciterName[]>;
  en: Record<string, ReciterName[]>;
};

const Extension = () => {
  const {
    surahsList,
    searchResult,
    lang,
    chooseReciter,
    playing,
    playlist,
    qari,
    pageWidth,
  } = useContext<GlobalStatesContext>(GlobalStates);
  const availableSurahs: JSX.Element[] = [];
  const avaialbeReciters: JSX.Element[] = [];
  const scrollTimeout = useRef<number | null>(null);
  const playingRef = useRef<number>(playing);
  const playlistRef = useRef<Play[]>(playlist);
  const offsetRef = useRef<number>(pageWidth <= 800 ? -165 : -120);
  const surahsListContainerRef = useRef(null);
  const scrollOptions = {
    duration: 700,
    smooth: true,
    offset: pageWidth <= 800 ? -165 : -120,
  };
  useEffect(() => {
    offsetRef.current = pageWidth <= 800 ? -165 : -120;
  }, [pageWidth]);
  useEffect(() => {
    const handleScroll = () => {
      clearTimeout(scrollTimeout.current as number);
      scrollTimeout.current = setTimeout(() => {
        scroller.scrollTo(
          String(String(playlistRef.current[playingRef.current]["id"])),
          { ...scrollOptions, offset: offsetRef.current }
        );
      }, 3500);
    };

    window.addEventListener("scroll", () => {
      handleScroll();
      if (surahsListContainerRef.current) {
        const surahsListContainer: HTMLElement = surahsListContainerRef.current;
        surahsListContainer.style.pointerEvents = "none";
      }
    });
    window.addEventListener("mousemove", () => {
      handleScroll();
      if (surahsListContainerRef.current) {
        const surahsListContainer: HTMLElement = surahsListContainerRef.current;
        surahsListContainer.style.pointerEvents = "initial";
      }
    });
    return () => {
      window.removeEventListener("scroll", handleScroll);
      window.removeEventListener("mousemove", handleScroll);
      clearTimeout(scrollTimeout.current as number);
    };
  }, []);

  useEffect(() => {
    scroller.scrollTo(
      String(String(playlistRef.current[playingRef.current]["id"])),
      { ...scrollOptions, duration: 0 }
    );
  }, [lang, qari]);
  useEffect(() => {
    playingRef.current = playing;
    playlistRef.current = playlist;
    // Set timeout to reset scroll status after 150ms of no scroll
    scroller.scrollTo(String(String(playlist[playing]["id"])), scrollOptions);
  }, [playing, playlist]);
  if (!chooseReciter) {
    surahsList.forEach(
      ({ id, name, start_page, end_page, makkia, type }, index) => {
        if (
          name[lang as keyof typeof name]
            .toLowerCase()
            .startsWith(searchResult.trim().toLowerCase()) ||
          String(id).startsWith(searchResult.trim())
        ) {
          availableSurahs.push(
            <Element name={String(id)}>
              <Surah
                id={id}
                name={name}
                start_page={start_page}
                end_page={end_page}
                makkia={makkia}
                type={type}
                key={index}
              />
            </Element>
          );
        }
      }
    );
  } else {
    const reciterNamesTyped = reciterNames as ReciterNamesType;
    const langReciters = reciterNamesTyped[lang as keyof ReciterNamesType];

    Object.keys(langReciters).forEach((firstLetter) => {
      const reciters = langReciters[firstLetter];
      if (
        reciters.some(({ name }) =>
          name.toLowerCase().startsWith(searchResult.trim().toLowerCase())
        )
      ) {
        avaialbeReciters.push(
          <ReciterList key={firstLetter} firstLetter={firstLetter} />
        );
      }
    });
  }

  return (
    <div>
      <Header />
      {chooseReciter ? (
        avaialbeReciters.length >= 1 ? (
          <div style={{ pointerEvents: "all" }} className="reciters-grid">
            {Object.keys(
              (reciterNames as ReciterNamesType)[lang as keyof ReciterNamesType]
            ).map((firstLetter) => (
              <ReciterList key={firstLetter} firstLetter={firstLetter} />
            ))}
          </div>
        ) : (
          <NotFound
            comment={
              lang == "en"
                ? "No reciter found. Try a different name or check the spelling."
                : "لم يتم العثور على قارئ. جرّب اسمًا مختلفًا أو تحقق من طريقة الكتابة."
            }
          />
        )
      ) : !availableSurahs.length ? (
        <NotFound
          comment={
            lang == "en"
              ? "No Surah found. Try checking the spelling or using the Surah number."
              : "لم يتم العثور على سورة. حاول التحقق من طريقة الكتابة أو استخدام رقم السورة."
          }
        />
      ) : (
        <div ref={surahsListContainerRef}>{availableSurahs}</div>
      )}

      <Player />
    </div>
  );
};
export default Extension;
