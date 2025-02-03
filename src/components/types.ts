export interface SurahData {
    id: number;
    name: {
      arabicName: string;
      englishName: string;
      literalName: string;
    };
    playing: boolean
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