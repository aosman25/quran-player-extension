import Player from "./Player";
import Surah from "./Surah";
import { GlobalStatesContext } from "../types";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";
import Header from "./Header";
import reciterNames from "../data/quranmp3/sorted_reciter_names.json";
import ReciterList from "./ReciterList";
import "../styles/components/Extension.scss";
import NotFound from "./NotFound";

const Extension = () => {
  const { surahsList, searchResult, lang, chooseReciter } =
    useContext<GlobalStatesContext>(GlobalStates);
  const availableSurahs: JSX.Element[] = [];
  const avaialbeReciters: JSX.Element[] = [];

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
            <Surah
              id={id}
              name={name}
              start_page={start_page}
              end_page={end_page}
              makkia={makkia}
              type={type}
              key={index}
            />
          );
        }
      }
    );
  } else {
    Object.keys(reciterNames[lang as keyof typeof reciterNames]).forEach(
      (firstLetter) => {
        if (
          reciterNames[lang][firstLetter].some(({ name }: { name: string }) =>
            name.toLowerCase().startsWith(searchResult.trim().toLowerCase())
          )
        ) {
          avaialbeReciters.push(
            <ReciterList key={firstLetter} firstLetter={firstLetter} />
          );
        }
      }
    );
  }

  return (
    <div>
      <Header />
      {chooseReciter ? (
        avaialbeReciters.length >= 1 ? (
          <div className="reciters-grid">
            {Object.keys(reciterNames[lang as keyof typeof reciterNames]).map(
              (firstLetter) => (
                <ReciterList key={firstLetter} firstLetter={firstLetter} />
              )
            )}
          </div>
        ) : (
          <NotFound comment="No reciter found. Try a different name or check the spelling." />
        )
      ) : !availableSurahs.length ? (
        <NotFound comment="No Surah found. Try checking the spelling or using the Surah number." />
      ) : (
        availableSurahs
      )}

      <Player />
    </div>
  );
};
export default Extension;
