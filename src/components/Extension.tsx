import Player from "./Player";
import Surah from "./Surah";
import { GlobalStatesContext } from "../types";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";

const Extension = () => {
  const { surahsList } = useContext<GlobalStatesContext>(GlobalStates);
  return (
    <div>
      {surahsList.map(({ id, name }, index) => {
        return <Surah id={id} name={name} key={index} />;
      })}

      <Player />
    </div>
  );
};
export default Extension;
