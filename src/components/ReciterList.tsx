import { useContext } from "react";
import reciterNames from "../data/quranmp3/sorted_reciter_names.json";
import { GlobalStates } from "../GlobalStates";
import "../styles/components/ReciterList.scss";

type ReciterName = {
  id: number;
  name: string;
};

type ReciterNamesType = {
  ar: Record<string, ReciterName[]>;
  en: Record<string, ReciterName[]>;
};

const ReciterList = ({ firstLetter }: { firstLetter: string }) => {
  const {
    lang,
    setChooseReciter,
    setQari,
    setPlaying,
    setMoshaf,
    searchResult,
    setSearchResult,
    extensionMode,
  } = useContext(GlobalStates);
  const availableQaris: JSX.Element[] = [];

  const reciterNamesTyped = reciterNames as ReciterNamesType;
  const langReciters = reciterNamesTyped[lang as keyof ReciterNamesType];
  const reciters = langReciters[firstLetter] || [];

  reciters.forEach(({ name, id }) => {
    if (name.toLowerCase().startsWith(searchResult.trim().toLowerCase())) {
      availableQaris.push(
        <button
          className={`${lang == "en" ? "en-font" : "ar-font"}`}
          key={id}
          onClick={() => {
            setChooseReciter(false);
            setQari(id);
            setPlaying(0);
            setMoshaf(0);
            setSearchResult("");
            if (extensionMode) {
              const extensionData = JSON.parse(
                localStorage.getItem("quranstream-extension") || "{}"
              );
              localStorage.setItem(
                "quranstream-extension",
                JSON.stringify({
                  ...extensionData,
                  playing: 0,
                  moshaf: 0,
                  qari: id,
                })
              );
            }
          }}
        >
          {name}
        </button>
      );
    }
  });

  return availableQaris.length >= 1 &&
    (!searchResult ||
      firstLetter
        .toLowerCase()
        .startsWith(searchResult.trim()[0].toLowerCase())) ? (
    <div className="reciter-list">
      <div>
        <p className={`first-letter ${lang == "en" ? "en-font" : "ar-font"}`}>
          {firstLetter}
        </p>
        <hr />
      </div>
      <div className="reciter-sublist">{availableQaris}</div>
    </div>
  ) : null;
};

export default ReciterList;
