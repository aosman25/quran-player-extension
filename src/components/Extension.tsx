import Player from "./Player";
import Surah from "./Surah";
import { GlobalStatesContext } from "../types";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";
import Header from "./Header";

const Extension = () => {
  const { surahsList, searchResult, lang } =
    useContext<GlobalStatesContext>(GlobalStates);
  return (
    <div>
      <Header />
      {surahsList.map(
        ({ id, name, start_page, end_page, makkia, type }, index) => {
          return name[lang as keyof typeof name]
            .toLowerCase()
            .startsWith(searchResult.trim()) ||
            String(id).startsWith(searchResult.trim()) ? (
            <Surah
              id={id}
              name={name}
              start_page={start_page}
              end_page={end_page}
              makkia={makkia}
              type={type}
              key={index}
            />
          ) : null;
        }
      )}

      <Player />
    </div>
  );
};
export default Extension;
