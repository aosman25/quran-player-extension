import { SurahData } from "./types";
import "../styles/components/Surah.scss";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext } from "../types";
const Surah = ({ id, name, playing }: SurahData) => {
  const { englishName, literalName } = name;
  const { setPlaying, qari } = useContext<GlobalStatesContext>(GlobalStates);
  const onClick = () => {
    setPlaying({
      qariID: qari,
      surahID: id,
    });
  };
  return (
    <>
      <div
        style={playing ? { backgroundColor: "#1DB954" } : {}}
        onClick={onClick}
        className="surah-box"
      >
        <div>{id}</div>
        <div>{literalName}</div>
        <div>
          <i>{englishName}</i>
        </div>
      </div>
      <hr />
    </>
  );
};
export default Surah;
