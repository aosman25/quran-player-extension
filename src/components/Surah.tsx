import { SurahData } from "../types";
import "../styles/components/Surah.scss";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";
import { GlobalStatesContext } from "../types";
const Surah = ({ id, name }: SurahData) => {
  const { playing, playlist, lang } =
    useContext<GlobalStatesContext>(GlobalStates);
  const { setPlaying } = useContext<GlobalStatesContext>(GlobalStates);
  const onClick = () => {
    setPlaying(playlist.findIndex(({ id: surahId }) => surahId == id));
  };
  return (
    <>
      <div
        style={
          playing == playlist.findIndex(({ id: surahId }) => surahId == id)
            ? { backgroundColor: "#1DB954" }
            : {}
        }
        onClick={onClick}
        className="surah-box"
      >
        <div>{id}</div>
        <div>{name[lang as keyof typeof name]}</div>
        <div></div>
      </div>
      <hr />
    </>
  );
};
export default Surah;
