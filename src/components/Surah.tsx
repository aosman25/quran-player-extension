import { SurahData } from "./types";
import "../styles/components/Surah.scss";
const Surah = ({ id, name }: SurahData) => {
  const { englishName, literalName } = name;
  return (
    <>
      <div className="surah-box">
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
