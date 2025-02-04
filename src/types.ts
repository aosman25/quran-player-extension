
export interface GlobalStatesContext {
    playlist: Play[],
    setPlaylist: React.Dispatch<React.SetStateAction<Play[]>>,
    playing: number,
    setPlaying: React.Dispatch<React.SetStateAction<number>>,
    qari: number,
    setQari: React.Dispatch<React.SetStateAction<number>>,
    surahsList: SurahData[]
}

export interface Play {
    name: string,
    writer: string,
    src:  string,
    id: number,
}

export interface rawReciterData {
    id: number,
    name: string,
    arabicName: string,
    relativePath: string,
    fileFormats: string,
    sectionId: number,
    home: boolean,
    description: null,
    torrentFilename: string
    torrentInfoHash: string,
    torrentSeeders: number,
    torrentLeechers: number,
    letter: string
}

export interface SurahData {
    id: number;
    name: {
      arabicName: string;
      englishName: string;
      literalName: string;
    };
  }

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