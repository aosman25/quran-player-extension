import { useContext } from "react";
import reciterNames from "../data/quranmp3/sorted_reciter_names.json";
import { GlobalStates } from "../GlobalStates";
import "../styles/components/ReciterList.scss";

const ReciterList = ({ firstLetter }: { firstLetter: string }) => {
  const {
    lang,
    setChooseReciter,
    setQari,
    setPlaying,
    setMoshaf,
    searchResult,
    setSearchResult,
  } = useContext(GlobalStates);
  const availableQaris: JSX.Element[] = [];
  reciterNames[lang][firstLetter].forEach(
    ({ name, id }: { name: string; id: number }) => {
      if (name.toLowerCase().startsWith(searchResult.trim().toLowerCase())) {
        availableQaris.push(
          <button
            onClick={() => {
              setChooseReciter(false);
              setQari(id);
              setPlaying(0);
              setMoshaf(0);
              setSearchResult("");
            }}
          >
            {name}
          </button>
        );
      }
    }
  );
  return availableQaris.length >= 1 &&
    (!searchResult ||
      firstLetter
        .toLowerCase()
        .startsWith(searchResult.trim()[0].toLowerCase())) ? (
    <div className="reciter-list">
      <div>
        <p>{firstLetter}</p>
        <hr />
      </div>
      <div className="reciter-sublist">{availableQaris}</div>
    </div>
  ) : null;
};

export default ReciterList;
