export interface SurahData {
    id: string;
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