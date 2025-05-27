import { createContext } from "react";
import { GlobalStatesContext, Play, PlayOptions, SurahData } from "./types";

const defaultGlobalStates: GlobalStatesContext = {
  playlist: [] as Play[],
  setPlaylist: () => {},
  playing: 0,
  setPlaying: () => {},
  qari: 0,
  setQari: () => {},
  surahsList: [] as SurahData[],
  lang: "en",
  setLang: () => {},
  moshaf: 0,
  setMoshaf: () => {},
  loved: false,
  setLoved: () => {},
  searchResult: "",
  setSearchResult: () => {},
  chooseReciter: false,
  setChooseReciter: () => {},
  notFound: false,
  setNotFound: () => {},
  playOptions: {
    playing: false,
    duration: 0,
    currentTime: 0,
  } as PlayOptions,
  setPlayOptions: () => {},
  pageWidth: 0,
  setPageWidth: () => {},
  extensionMode: false,
  isLoading: false,
  setIsLoading: () => {},
  isScrolling: false,
  storageKey: "",
};

export const GlobalStates =
  createContext<GlobalStatesContext>(defaultGlobalStates);
