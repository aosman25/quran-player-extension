import { useContext } from "react";
import reciterNames from "../data/quranmp3/sorted_reciter_names.json";
import { GlobalStates } from "../GlobalStates";
import { MoshafsType, ReciterNamesType } from "../types";
import recitersList from "../data/quranmp3/reciters.json";
import moshafsData from "../data/quranmp3/moshafs.json";
import "../styles/components/ReciterList.scss";
import {} from "../types";

const ReciterList = ({ firstLetter }: { firstLetter: string }) => {
  const {
    lang,
    setChooseReciter,
    qari,
    setQari,
    setPlaying,
    playing,
    setMoshaf,
    setSearchResult,
    setCleanedSearchResult,
    setPlayOptions,
    storageKey,
    extensionMode,
    cleanedSearchResult,
  } = useContext(GlobalStates);
  const availableQaris: JSX.Element[] = [];
  const moshafs: MoshafsType = moshafsData;

  const reciterNamesTyped = reciterNames as ReciterNamesType;
  const langReciters = reciterNamesTyped[lang as keyof ReciterNamesType];
  const reciters = langReciters[firstLetter] || [];

  reciters.forEach(({ name, id, search_combs }) => {
    const match = search_combs.some((n) => n.startsWith(cleanedSearchResult));

    if (match) {
      availableQaris.push(
        <button
          className={`${lang == "en" ? "en-font" : "ar-font"}`}
          key={id}
          onClick={() => {
            // Step 1: Get and sort the moshafs for this qari
            const availableMoshafs = recitersList[
              String(id) as keyof typeof recitersList
            ]["moshaf"].map(({ moshaf_id, moshaf_type }) => {
              return {
                moshaf_id,
                moshaf_type,
              };
            });
            const sorted = availableMoshafs
              .map((m, i) => ({ ...m, originalIndex: i }))
              .sort((a, b) => {
                const popA =
                  moshafs[a.moshaf_id][a.moshaf_type]?.popularity ?? 0;
                const popB =
                  moshafs[b.moshaf_id][b.moshaf_type]?.popularity ?? 0;
                return popB - popA;
              });

            // Step 2: Get the original index of the top (most popular) moshaf
            const topOriginalIndex = sorted[0]?.originalIndex ?? 0;
            setChooseReciter(false);
            if (qari !== id) {
              setQari(id);
              setPlayOptions({ playing: true, duration: 0, currentTime: 0 });
              setPlaying(0);
              setMoshaf(topOriginalIndex);
              setSearchResult("");
              setCleanedSearchResult("");
              if (extensionMode) {
                chrome.runtime.sendMessage({
                  type: "STOP_AUDIO",
                });
              }
              // Step 3: Update state and localStorage
              const storedData = JSON.parse(
                localStorage.getItem(storageKey) || "{}"
              );
              localStorage.setItem(
                storageKey,
                JSON.stringify({
                  ...storedData,
                  playing: 0,
                  moshaf: topOriginalIndex,
                  currentTime: 0,
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
  return (
    availableQaris.length >= 1 && (
      <div className="reciter-list">
        <div>
          <p className={`first-letter ${lang == "en" ? "en-font" : "ar-font"}`}>
            {firstLetter}
          </p>
          <hr />
        </div>
        <div className="reciter-sublist">{availableQaris}</div>
      </div>
    )
  );
};

export default ReciterList;
