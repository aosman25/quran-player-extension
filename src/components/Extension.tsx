import Player from "./Player";
import surahs from "../data/surahs.json";
import Surah from "./Surah";
import { SurahData } from "./types";

const Extension = () => {
  const surahsList: SurahData[] = [];

  for (const [id, surah] of Object.entries(surahs)) {
    const { simple, english, arabic } = surah.name;
    surahsList.push({
      id,
      name: {
        englishName: english,
        literalName: simple,
        arabicName: arabic,
      },
    });
  }
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
