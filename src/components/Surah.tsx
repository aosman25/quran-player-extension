import { SurahData } from "../types";
import "../styles/components/Surah.scss";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext } from "../types";
const Surah = ({ id, name }: SurahData) => {
  const { playing } = useContext<GlobalStatesContext>(GlobalStates);
  const { englishName, literalName } = name;
  const { setPlaying } = useContext<GlobalStatesContext>(GlobalStates);
  const onClick = () => {
    setPlaying(id);
  };
  return (
    <>
      <div
        style={playing == id ? { backgroundColor: "#1DB954" } : {}}
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
