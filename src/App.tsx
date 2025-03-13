import "./styles/index.scss";
import "./components/Extension";
import Extension from "./components/Extension";
import { GlobalStates } from "./GlobalStates";
import { useCallback, useState } from "react";
import { Play, rawReciterData } from "./types";
import surahs from "./data/quranmp3/surahs.json";
import recitersList from "./data/quranmp3/reciters.json";
import { SurahData } from "./types";
import { useMemo } from "react";

function App() {
  const [qari, setQari] = useState<number>(123); // Default Mishari Alafasi
  const [moshaf, setMoshaf] = useState<number>(1); // Default Moshaf
  const [lang, setLang] = useState<"en" | "ar">("en");
  const [playing, setPlaying] = useState<number>(0);
  const genrateSurahs = useCallback((): SurahData[] => {
    const surahsList: SurahData[] = [];
    const availableSurahs =
      recitersList[String(qari) as keyof typeof recitersList]["moshaf"][moshaf][
        "surah_list"
      ];
    for (const surah of availableSurahs) {
      surahsList.push(surahs[String(surah) as keyof typeof surahs]);
    }
    return surahsList;
  }, [moshaf, qari]);
  const surahsList: SurahData[] = useMemo(genrateSurahs, [genrateSurahs]);
  const generatePlaylist = useCallback(
    (qari: number): Play[] => {
      const playlist: Play[] = [];
      const reciter: rawReciterData = recitersList[
        String(qari) as keyof typeof recitersList
      ] as rawReciterData;

      surahsList.forEach(({ id }) => {
        const prefix = "000";
        const baseURL = reciter["moshaf"][moshaf]["server"];
        const fileFormat = ".mp3";

        playlist.push({
          id,
          name: surahs[String(id) as keyof typeof surahs]["name"][lang],
          writer: reciter.name[lang],
          src:
            baseURL +
            prefix.slice(0, prefix.length - String(id).length) +
            String(id) +
            fileFormat,
        });
      });
      return playlist;
    },
    [surahsList, lang, moshaf]
  );
  const [playlist, setPlaylist] = useState<Play[]>(generatePlaylist(qari));
  return (
    <GlobalStates.Provider
      value={{
        playlist,
        setPlaylist,
        playing,
        setPlaying,
        qari,
        setQari,
        surahsList,
        lang,
        setLang,
        moshaf,
        setMoshaf,
      }}
    >
      <Extension />
    </GlobalStates.Provider>
  );
}

export default App;
