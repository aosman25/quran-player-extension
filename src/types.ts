export interface GlobalStatesContext {
    playlist: Play[],
    setPlaylist: React.Dispatch<React.SetStateAction<Play[]>>,
    playing: number,
    setPlaying: React.Dispatch<React.SetStateAction<number>>,
    qari: number,
    setQari: React.Dispatch<React.SetStateAction<number>>,
    surahsList: SurahData[],
    lang: string,
    setLang: React.Dispatch<React.SetStateAction<"en" | "ar">>,
    moshaf: number,
    setMoshaf: React.Dispatch<React.SetStateAction<number>>,
    loved: boolean,
    setLoved: React.Dispatch<React.SetStateAction<boolean>>,
    searchResult: string,
    setSearchResult: React.Dispatch<React.SetStateAction<string>>,
    chooseReciter: boolean,
    setChooseReciter: React.Dispatch<React.SetStateAction<boolean>>,
    notFound: boolean,
    setNotFound: React.Dispatch<React.SetStateAction<boolean>>,
    playOptions: PlayOptions ,
    setPlayOptions: React.Dispatch<React.SetStateAction<PlayOptions>>,
    pageWidth: number,
    setPageWidth: React.Dispatch<React.SetStateAction<number>>,
    extensionMode: boolean,
    isLoading: boolean,
    setIsLoading: React.Dispatch<React.SetStateAction<boolean>>,
    isScrolling: boolean,
    storageKey: string
}


export interface PlayOptions {
  playing: boolean,
  duration: number,
  currentTime: number,
}
export interface Play {
    name: string,
    writer: string,
    src:  string,
    id: number,
}

export interface rawReciterData {
    id: number,
    name: Language,
    letter: Language,
    date: string,
    moshaf: moshaf[]
  }
interface moshaf{
  moshaf_id: number,
  moshaf_type: number,
  surah_total: number,
  server: string,
  surah_list: number[]
}

export interface Language {
  ar: string,
  en: string
}
export interface SurahData {
  id: number,
  name: {
      ar: string,
      en: string
  },
  start_page: number,
  end_page: number,
  makkia: number,
  type: number
}

export interface MoshafsType {
  [key: string | number]: {
    [key: string]: {
      "name": Language
      "popularity": number
    },
  }
}

export type ReciterName = {
  id: number;
  name: string;
  search_combs: string[];
};

export type ReciterNamesType = {
  ar: Record<string, ReciterName[]>;
  en: Record<string, ReciterName[]>;
};

export interface rawSurahData {
        "id": number,
        "page": [number, number],
        "bismillahPre": boolean,
        "ayat": number,
        "name": {
          "complex": string,
          "simple": string,
          "english":string,
          "arabic": string
        },
        "revelation": {
          "place": string,
          "order": number
        }
    }