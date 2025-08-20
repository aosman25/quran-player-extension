import Player from "./Player";
import Surah from "./Surah";
import { GlobalStatesContext, ReciterNamesType } from "../types";
import { useContext, useEffect, useRef } from "react";
import { GlobalStates } from "../GlobalStates";
import Header from "./Header";
import reciterNames from "../data/quranmp3/sorted_reciter_names.json";
import ReciterList from "./ReciterList";
import "../styles/components/Extension.scss";
import { Element } from "react-scroll";
import NotFound from "./NotFound";
import { useAutoScroll } from "../hooks/useAutoScroll";
import { SCROLL_DURATIONS } from "../constants/scrollConfig";

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
    cleanedSearchResult,
  } = useContext<GlobalStatesContext>(GlobalStates);
  const availableSurahs: JSX.Element[] = [];
  const availableReciters: JSX.Element[] = [];
  const surahsListContainerRef = useRef(null);

  // Use the centralized auto-scroll hook
  const { scrollToCurrentItem, setupAutoScrollOnUserActivity } = useAutoScroll({
    playlist,
    playing,
    pageWidth,
  });
  useEffect(() => {
    // Setup auto-scroll behavior on user activity
    return setupAutoScrollOnUserActivity(surahsListContainerRef);
  }, [setupAutoScrollOnUserActivity]);

  useEffect(() => {
    scrollToCurrentItem(SCROLL_DURATIONS.INSTANT);
  }, [lang, qari, chooseReciter, scrollToCurrentItem]);

  useEffect(() => {
    scrollToCurrentItem(SCROLL_DURATIONS.AUTO_SCROLL_DELAY);
  }, [playing, playlist, scrollToCurrentItem]);
  if (!chooseReciter) {
    surahsList.forEach(
      ({ id, name, start_page, end_page, makkia, type }, index) => {
        if (
          name[lang as keyof typeof name]
            .toLowerCase()
            .replace(/-/g, "")
            .replace(/'/g, "")
            .includes(cleanedSearchResult) ||
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
      let match = false;
      reciters.forEach(({ search_combs }) => {
        if (search_combs.some((n) => n.startsWith(cleanedSearchResult))) {
          match = true;
        }
      });
      if (match) {
        availableReciters.push(
          <ReciterList key={firstLetter} firstLetter={firstLetter} />
        );
      }
    });
  }
  return (
    <div>
      <Header />
      {chooseReciter ? (
        availableReciters.length >= 1 ? (
          <div style={{ pointerEvents: "all" }} className="reciters-grid">
            {availableReciters}
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
