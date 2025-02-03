import Player from "./Player";
import surahs from "../data/surahs.json";
import Surah from "./Surah";
import { SurahData } from "./types";
import { useContext } from "react";
import { GlobalStates } from "../GlobalStates";

const Extension = () => {
  const surahsList: SurahData[] = [];
  const { playing } = useContext(GlobalStates);
  for (const [id, surah] of Object.entries(surahs)) {
    const { simple, english, arabic } = surah.name;
    surahsList.push({
      id: Number(id),
      name: {
        englishName: english,
        literalName: simple,
        arabicName: arabic,
      },
      playing: playing.surahID == Number(id),
    });
  }
  return (
    <div>
      {surahsList.map(({ id, name, playing }, index) => {
        return <Surah id={id} name={name} key={index} playing={playing} />;
      })}

      <Player />
    </div>
  );
};
export default Extension;
