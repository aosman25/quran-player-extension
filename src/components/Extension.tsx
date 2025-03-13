import Player from "./Player";
import Surah from "./Surah";
import { GlobalStatesContext } from "../types";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";

const Extension = () => {
  const { surahsList } = useContext<GlobalStatesContext>(GlobalStates);
  return (
    <div>
      {surahsList.map(
        ({ id, name, start_page, end_page, makkia, type }, index) => {
          return (
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
      )}

      <Player />
    </div>
  );
};
export default Extension;
