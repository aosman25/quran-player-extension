import "./styles/index.scss";
import "./components/Extension";
import Extension from "./components/Extension";
import { GlobalStates } from "./GlobalStates";
import { useCallback, useState } from "react";
import { Play, rawReciterData } from "./types";
import recitersList from "./data/reciters.json";
import surahs from "./data/surahs.json";
import { SurahData } from "./types";
import { useMemo } from "react";

function App() {
  const [qari, setQari] = useState<number>(5); // Default Mishari Alafasi
  const [moshaf, setMoshaf] = useState<number>(1); // Default Moshaf
  const [lang, setLang] = useState<"en" | "ar">("en");
  const [playing, setPlaying] = useState<number>(0);
  const genrateSurahs = useCallback((): SurahData[] => {
    const surahsList: SurahData[] = [];
    for (const [id, surah] of Object.entries(surahs)) {
      const { simple, english, arabic } = surah.name;
      surahsList.push({
        id: Number(id),
        name: {
          englishName: english,
          literalName: simple,
          arabicName: arabic,
        },
      });
    }
    return surahsList;
  }, []);
  const surahsList: SurahData[] = useMemo(genrateSurahs, [genrateSurahs]);
  const generatePlaylist = useCallback(
    (qari: number): Play[] => {
      const playlist: Play[] = [];
      const reciter: rawReciterData = recitersList[
        String(qari) as keyof typeof recitersList
      ] as rawReciterData;

      surahsList.forEach(({ id, name }) => {
        const prefix = "000";
        const baseURL = "https://download.quranicaudio.com/quran/";
        const fileFormat = "." + reciter.fileFormats;
        const relativePath = reciter.relativePath;
        playlist.push({
          id,
          name: name.literalName,
          writer: reciter.name,
          src:
            baseURL +
            relativePath +
            prefix.slice(0, prefix.length - String(id).length) +
            String(id) +
            fileFormat,
        });
      });
      return playlist;
    },
    [surahsList]
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
      }}
    >
      <Extension />
    </GlobalStates.Provider>
  );
}

export default App;
