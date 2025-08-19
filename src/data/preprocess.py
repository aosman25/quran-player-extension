import json
from collections import defaultdict
import re


ar_surahs =  [
    {
      "id": 1,
      "name": "الفاتحة",
      "start_page": 1,
      "end_page": 1,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 2,
      "name": "البقرة",
      "start_page": 2,
      "end_page": 49,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 3,
      "name": "آل عمران",
      "start_page": 50,
      "end_page": 76,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 4,
      "name": "النساء",
      "start_page": 77,
      "end_page": 106,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 5,
      "name": "المائدة",
      "start_page": 106,
      "end_page": 127,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 6,
      "name": "الأنعام",
      "start_page": 128,
      "end_page": 150,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 7,
      "name": "الأعراف",
      "start_page": 151,
      "end_page": 176,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 8,
      "name": "الأنفال",
      "start_page": 177,
      "end_page": 186,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 9,
      "name": "التوبة",
      "start_page": 187,
      "end_page": 207,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 10,
      "name": "يونس",
      "start_page": 208,
      "end_page": 221,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 11,
      "name": "هود",
      "start_page": 221,
      "end_page": 235,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 12,
      "name": "يوسف",
      "start_page": 235,
      "end_page": 248,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 13,
      "name": "الرعد",
      "start_page": 249,
      "end_page": 255,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 14,
      "name": "إبراهيم",
      "start_page": 255,
      "end_page": 261,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 15,
      "name": "الحجر",
      "start_page": 262,
      "end_page": 267,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 16,
      "name": "النحل",
      "start_page": 267,
      "end_page": 281,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 17,
      "name": "الإسراء",
      "start_page": 282,
      "end_page": 293,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 18,
      "name": "الكهف",
      "start_page": 293,
      "end_page": 304,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 19,
      "name": "مريم",
      "start_page": 305,
      "end_page": 312,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 20,
      "name": "طه",
      "start_page": 312,
      "end_page": 321,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 21,
      "name": "الأنبياء",
      "start_page": 322,
      "end_page": 331,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 22,
      "name": "الحج",
      "start_page": 332,
      "end_page": 341,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 23,
      "name": "المؤمنون",
      "start_page": 342,
      "end_page": 349,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 24,
      "name": "النور",
      "start_page": 350,
      "end_page": 359,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 25,
      "name": "الفرقان",
      "start_page": 359,
      "end_page": 366,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 26,
      "name": "الشعراء",
      "start_page": 367,
      "end_page": 376,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 27,
      "name": "النمل",
      "start_page": 377,
      "end_page": 385,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 28,
      "name": "القصص",
      "start_page": 385,
      "end_page": 396,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 29,
      "name": "العنكبوت",
      "start_page": 396,
      "end_page": 404,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 30,
      "name": "الروم",
      "start_page": 404,
      "end_page": 410,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 31,
      "name": "لقمان",
      "start_page": 411,
      "end_page": 414,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 32,
      "name": "السجدة",
      "start_page": 415,
      "end_page": 417,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 33,
      "name": "الأحزاب",
      "start_page": 418,
      "end_page": 427,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 34,
      "name": "سبأ",
      "start_page": 428,
      "end_page": 434,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 35,
      "name": "فاطر",
      "start_page": 434,
      "end_page": 440,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 36,
      "name": "يس",
      "start_page": 440,
      "end_page": 445,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 37,
      "name": "الصافات",
      "start_page": 446,
      "end_page": 452,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 38,
      "name": "ص",
      "start_page": 453,
      "end_page": 458,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 39,
      "name": "الزمر",
      "start_page": 458,
      "end_page": 467,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 40,
      "name": "غافر",
      "start_page": 467,
      "end_page": 476,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 41,
      "name": "فصلت",
      "start_page": 477,
      "end_page": 482,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 42,
      "name": "الشورى",
      "start_page": 483,
      "end_page": 489,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 43,
      "name": "الزخرف",
      "start_page": 489,
      "end_page": 495,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 44,
      "name": "الدّخان",
      "start_page": 496,
      "end_page": 498,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 45,
      "name": "الجاثية",
      "start_page": 499,
      "end_page": 502,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 46,
      "name": "الأحقاف",
      "start_page": 502,
      "end_page": 506,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 47,
      "name": "محمد",
      "start_page": 507,
      "end_page": 510,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 48,
      "name": "الفتح",
      "start_page": 511,
      "end_page": 515,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 49,
      "name": "الحجرات",
      "start_page": 515,
      "end_page": 517,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 50,
      "name": "ق",
      "start_page": 518,
      "end_page": 520,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 51,
      "name": "الذاريات",
      "start_page": 520,
      "end_page": 523,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 52,
      "name": "الطور",
      "start_page": 523,
      "end_page": 525,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 53,
      "name": "النجم",
      "start_page": 526,
      "end_page": 528,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 54,
      "name": "القمر",
      "start_page": 528,
      "end_page": 531,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 55,
      "name": "الرحمن",
      "start_page": 531,
      "end_page": 534,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 56,
      "name": "الواقعة",
      "start_page": 534,
      "end_page": 537,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 57,
      "name": "الحديد",
      "start_page": 537,
      "end_page": 541,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 58,
      "name": "المجادلة",
      "start_page": 542,
      "end_page": 545,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 59,
      "name": "الحشر",
      "start_page": 545,
      "end_page": 548,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 60,
      "name": "الممتحنة",
      "start_page": 549,
      "end_page": 551,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 61,
      "name": "الصف",
      "start_page": 551,
      "end_page": 552,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 62,
      "name": "الجمعة",
      "start_page": 553,
      "end_page": 554,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 63,
      "name": "المنافقون",
      "start_page": 554,
      "end_page": 555,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 64,
      "name": "التغابن",
      "start_page": 556,
      "end_page": 557,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 65,
      "name": "الطلاق",
      "start_page": 558,
      "end_page": 559,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 66,
      "name": "التحريم",
      "start_page": 560,
      "end_page": 561,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 67,
      "name": "الملك",
      "start_page": 562,
      "end_page": 564,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 68,
      "name": "القلم",
      "start_page": 564,
      "end_page": 566,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 69,
      "name": "الحاقة",
      "start_page": 566,
      "end_page": 568,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 70,
      "name": "المعارج",
      "start_page": 568,
      "end_page": 570,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 71,
      "name": "نوح",
      "start_page": 570,
      "end_page": 571,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 72,
      "name": "الجن",
      "start_page": 572,
      "end_page": 573,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 73,
      "name": "المزمل",
      "start_page": 574,
      "end_page": 575,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 74,
      "name": "المدثر",
      "start_page": 575,
      "end_page": 577,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 75,
      "name": "القيامة",
      "start_page": 577,
      "end_page": 578,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 76,
      "name": "الإنسان",
      "start_page": 578,
      "end_page": 580,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 77,
      "name": "المرسلات",
      "start_page": 580,
      "end_page": 581,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 78,
      "name": "النبأ",
      "start_page": 582,
      "end_page": 583,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 79,
      "name": "النازعات",
      "start_page": 583,
      "end_page": 584,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 80,
      "name": "عبس",
      "start_page": 585,
      "end_page": 586,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 81,
      "name": "التكوير",
      "start_page": 586,
      "end_page": 586,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 82,
      "name": "الإنفطار",
      "start_page": 587,
      "end_page": 587,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 83,
      "name": "المطففين",
      "start_page": 587,
      "end_page": 589,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 84,
      "name": "الإنشقاق",
      "start_page": 589,
      "end_page": 590,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 85,
      "name": "البروج",
      "start_page": 590,
      "end_page": 590,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 86,
      "name": "الطارق",
      "start_page": 591,
      "end_page": 591,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 87,
      "name": "الأعلى",
      "start_page": 591,
      "end_page": 592,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 88,
      "name": "الغاشية",
      "start_page": 592,
      "end_page": 593,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 89,
      "name": "الفجر",
      "start_page": 593,
      "end_page": 594,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 90,
      "name": "البلد",
      "start_page": 594,
      "end_page": 595,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 91,
      "name": "الشمس",
      "start_page": 595,
      "end_page": 595,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 92,
      "name": "الليل",
      "start_page": 595,
      "end_page": 596,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 93,
      "name": "الضحى",
      "start_page": 596,
      "end_page": 596,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 94,
      "name": "الشرح",
      "start_page": 596,
      "end_page": 597,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 95,
      "name": "التين",
      "start_page": 597,
      "end_page": 597,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 96,
      "name": "العلق",
      "start_page": 597,
      "end_page": 598,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 97,
      "name": "القدر",
      "start_page": 598,
      "end_page": 598,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 98,
      "name": "البينة",
      "start_page": 598,
      "end_page": 599,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 99,
      "name": "الزلزلة",
      "start_page": 599,
      "end_page": 599,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 100,
      "name": "العاديات",
      "start_page": 599,
      "end_page": 600,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 101,
      "name": "القارعة",
      "start_page": 600,
      "end_page": 600,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 102,
      "name": "التكاثر",
      "start_page": 600,
      "end_page": 600,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 103,
      "name": "العصر",
      "start_page": 601,
      "end_page": 601,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 104,
      "name": "الهمزة",
      "start_page": 601,
      "end_page": 601,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 105,
      "name": "الفيل",
      "start_page": 601,
      "end_page": 601,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 106,
      "name": "قريش",
      "start_page": 602,
      "end_page": 602,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 107,
      "name": "الماعون",
      "start_page": 602,
      "end_page": 602,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 108,
      "name": "الكوثر",
      "start_page": 602,
      "end_page": 602,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 109,
      "name": "الكافرون",
      "start_page": 603,
      "end_page": 603,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 110,
      "name": "النصر",
      "start_page": 603,
      "end_page": 603,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 111,
      "name": "المسد",
      "start_page": 603,
      "end_page": 603,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 112,
      "name": "الإخلاص",
      "start_page": 604,
      "end_page": 604,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 113,
      "name": "الفلق",
      "start_page": 604,
      "end_page": 604,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 114,
      "name": "الناس",
      "start_page": 604,
      "end_page": 604,
      "makkia": 1,
      "type": 0
    }
  ]
en_surahs = [
    {
      "id": 1,
      "name": "Al-Fatihah ",
      "start_page": 1,
      "end_page": 1,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 2,
      "name": "Al-Baqarah ",
      "start_page": 2,
      "end_page": 49,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 3,
      "name": "Al-Imran ",
      "start_page": 50,
      "end_page": 76,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 4,
      "name": "An-Nisa' ",
      "start_page": 77,
      "end_page": 106,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 5,
      "name": "Al-Ma'idah ",
      "start_page": 106,
      "end_page": 127,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 6,
      "name": "Al-An'am ",
      "start_page": 128,
      "end_page": 150,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 7,
      "name": "Al-A'raf ",
      "start_page": 151,
      "end_page": 176,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 8,
      "name": "Al-Anfal ",
      "start_page": 177,
      "end_page": 186,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 9,
      "name": "At-Taubah ",
      "start_page": 187,
      "end_page": 207,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 10,
      "name": "Yunus ",
      "start_page": 208,
      "end_page": 221,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 11,
      "name": "Hood ",
      "start_page": 221,
      "end_page": 235,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 12,
      "name": "Yusuf ",
      "start_page": 235,
      "end_page": 248,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 13,
      "name": "Ar-Ra'd ",
      "start_page": 249,
      "end_page": 255,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 14,
      "name": "Ibrahim ",
      "start_page": 255,
      "end_page": 261,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 15,
      "name": "Al-Hijr ",
      "start_page": 262,
      "end_page": 267,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 16,
      "name": "An-Nahl ",
      "start_page": 267,
      "end_page": 281,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 17,
      "name": "Al-Isra ",
      "start_page": 282,
      "end_page": 293,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 18,
      "name": "Al-Kahf ",
      "start_page": 293,
      "end_page": 304,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 19,
      "name": "Maryam ",
      "start_page": 305,
      "end_page": 312,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 20,
      "name": "Ta­Ha ",
      "start_page": 312,
      "end_page": 321,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 21,
      "name": "Al-Anbiya' ",
      "start_page": 322,
      "end_page": 331,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 22,
      "name": "Al-Hajj ",
      "start_page": 332,
      "end_page": 341,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 23,
      "name": "Al-Mu'minun ",
      "start_page": 342,
      "end_page": 349,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 24,
      "name": "An-Nur ",
      "start_page": 350,
      "end_page": 359,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 25,
      "name": "Al-Furqan ",
      "start_page": 359,
      "end_page": 366,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 26,
      "name": "Ash-Shu'ara' ",
      "start_page": 367,
      "end_page": 376,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 27,
      "name": "An-Naml ",
      "start_page": 377,
      "end_page": 385,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 28,
      "name": "Al-Qasas ",
      "start_page": 385,
      "end_page": 396,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 29,
      "name": "Al-'Ankabut ",
      "start_page": 396,
      "end_page": 404,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 30,
      "name": "Ar­Room",
      "start_page": 404,
      "end_page": 410,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 31,
      "name": "Luqman ",
      "start_page": 411,
      "end_page": 414,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 32,
      "name": "As­Sajdah ",
      "start_page": 415,
      "end_page": 417,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 33,
      "name": "Al­Ahzab ",
      "start_page": 418,
      "end_page": 427,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 34,
      "name": "Saba' ",
      "start_page": 428,
      "end_page": 434,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 35,
      "name": "Fatir ",
      "start_page": 434,
      "end_page": 440,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 36,
      "name": "Ya­Sin ",
      "start_page": 440,
      "end_page": 445,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 37,
      "name": "As-Saffat ",
      "start_page": 446,
      "end_page": 452,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 38,
      "name": "Sad ",
      "start_page": 453,
      "end_page": 458,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 39,
      "name": "Az-Zumar ",
      "start_page": 458,
      "end_page": 467,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 40,
      "name": "Ghafir ",
      "start_page": 467,
      "end_page": 476,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 41,
      "name": "Fussilat ",
      "start_page": 477,
      "end_page": 482,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 42,
      "name": "Ash-Shura ",
      "start_page": 483,
      "end_page": 489,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 43,
      "name": "Az-Zukhruf ",
      "start_page": 489,
      "end_page": 495,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 44,
      "name": "Ad-Dukhan ",
      "start_page": 496,
      "end_page": 498,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 45,
      "name": "Al-Jathiya ",
      "start_page": 499,
      "end_page": 502,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 46,
      "name": "Al-Ahqaf ",
      "start_page": 502,
      "end_page": 506,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 47,
      "name": "Muhammad ",
      "start_page": 507,
      "end_page": 510,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 48,
      "name": "Al-Fath ",
      "start_page": 511,
      "end_page": 515,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 49,
      "name": "Al-Hujurat ",
      "start_page": 515,
      "end_page": 517,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 50,
      "name": "Qaf ",
      "start_page": 518,
      "end_page": 520,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 51,
      "name": "Az-Zariyat ",
      "start_page": 520,
      "end_page": 523,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 52,
      "name": "At-Tur ",
      "start_page": 523,
      "end_page": 525,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 53,
      "name": "An-Najm ",
      "start_page": 526,
      "end_page": 528,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 54,
      "name": "Al-Qamar ",
      "start_page": 528,
      "end_page": 531,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 55,
      "name": "Ar-Rahman ",
      "start_page": 531,
      "end_page": 534,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 56,
      "name": "Al-Waqi'ah ",
      "start_page": 534,
      "end_page": 537,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 57,
      "name": "Al-Hadid ",
      "start_page": 537,
      "end_page": 541,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 58,
      "name": "Al-Mujadilah ",
      "start_page": 542,
      "end_page": 545,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 59,
      "name": "Al-Hashr ",
      "start_page": 545,
      "end_page": 548,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 60,
      "name": "Al-Mumtahinah ",
      "start_page": 549,
      "end_page": 551,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 61,
      "name": "As-Saff ",
      "start_page": 551,
      "end_page": 552,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 62,
      "name": "Al-Jumu'ah ",
      "start_page": 553,
      "end_page": 554,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 63,
      "name": "Al-Munafiqun ",
      "start_page": 554,
      "end_page": 555,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 64,
      "name": "At-Taghabun ",
      "start_page": 556,
      "end_page": 557,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 65,
      "name": "At-Talaq ",
      "start_page": 558,
      "end_page": 559,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 66,
      "name": "At-Tahrim ",
      "start_page": 560,
      "end_page": 561,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 67,
      "name": "Al-Mulk ",
      "start_page": 562,
      "end_page": 564,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 68,
      "name": "Al-Qalam ",
      "start_page": 564,
      "end_page": 566,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 69,
      "name": "Al-Haqqah ",
      "start_page": 566,
      "end_page": 568,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 70,
      "name": "Al-Ma'arij ",
      "start_page": 568,
      "end_page": 570,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 71,
      "name": "Nooh ",
      "start_page": 570,
      "end_page": 571,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 72,
      "name": "Al-Jinn ",
      "start_page": 572,
      "end_page": 573,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 73,
      "name": "Al-Muzzammil ",
      "start_page": 574,
      "end_page": 575,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 74,
      "name": "Al-Muddaththir ",
      "start_page": 575,
      "end_page": 577,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 75,
      "name": "Al-Qiyamah ",
      "start_page": 577,
      "end_page": 578,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 76,
      "name": "Al-Insan ",
      "start_page": 578,
      "end_page": 580,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 77,
      "name": "Al-Mursalat",
      "start_page": 580,
      "end_page": 581,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 78,
      "name": "An-Naba' ",
      "start_page": 582,
      "end_page": 583,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 79,
      "name": "An-Nazi'at ",
      "start_page": 583,
      "end_page": 584,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 80,
      "name": "Abasa",
      "start_page": 585,
      "end_page": 586,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 81,
      "name": "At-Takwir ",
      "start_page": 586,
      "end_page": 586,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 82,
      "name": "Al-Infitar ",
      "start_page": 587,
      "end_page": 587,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 83,
      "name": "Al-Mutaffifin ",
      "start_page": 587,
      "end_page": 589,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 84,
      "name": "Al-Inshiqaq ",
      "start_page": 589,
      "end_page": 590,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 85,
      "name": "Al-Buruj ",
      "start_page": 590,
      "end_page": 590,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 86,
      "name": "At-Tariq ",
      "start_page": 591,
      "end_page": 591,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 87,
      "name": "Al-A'la ",
      "start_page": 591,
      "end_page": 592,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 88,
      "name": "Al-Ghashiyah ",
      "start_page": 592,
      "end_page": 593,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 89,
      "name": "Al-Fajr ",
      "start_page": 593,
      "end_page": 594,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 90,
      "name": "Al-Balad ",
      "start_page": 594,
      "end_page": 595,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 91,
      "name": "Ash-Shams ",
      "start_page": 595,
      "end_page": 595,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 92,
      "name": "Al-Lail ",
      "start_page": 595,
      "end_page": 596,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 93,
      "name": "Ad-Duha ",
      "start_page": 596,
      "end_page": 596,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 94,
      "name": "Ash-Sharh ",
      "start_page": 596,
      "end_page": 597,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 95,
      "name": "At-Tin ",
      "start_page": 597,
      "end_page": 597,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 96,
      "name": "Al-'Alaq ",
      "start_page": 597,
      "end_page": 598,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 97,
      "name": "Al-Qadr ",
      "start_page": 598,
      "end_page": 598,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 98,
      "name": "Al-Baiyinah ",
      "start_page": 598,
      "end_page": 599,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 99,
      "name": "Az-Zalzalah ",
      "start_page": 599,
      "end_page": 599,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 100,
      "name": "Al-'Adiyat ",
      "start_page": 599,
      "end_page": 600,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 101,
      "name": "Al-Qari'ah ",
      "start_page": 600,
      "end_page": 600,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 102,
      "name": "At-Takathur ",
      "start_page": 600,
      "end_page": 600,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 103,
      "name": "Al-'Asr ",
      "start_page": 601,
      "end_page": 601,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 104,
      "name": "Al-Humazah ",
      "start_page": 601,
      "end_page": 601,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 105,
      "name": "Al-Fil ",
      "start_page": 601,
      "end_page": 601,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 106,
      "name": "Quraish ",
      "start_page": 602,
      "end_page": 602,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 107,
      "name": "Al-Ma'un ",
      "start_page": 602,
      "end_page": 602,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 108,
      "name": "Al-Kauthar ",
      "start_page": 602,
      "end_page": 602,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 109,
      "name": "Al-Kafirun ",
      "start_page": 603,
      "end_page": 603,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 110,
      "name": "An-Nasr ",
      "start_page": 603,
      "end_page": 603,
      "makkia": 0,
      "type": 1
    },
    {
      "id": 111,
      "name": "Al-Masad ",
      "start_page": 603,
      "end_page": 603,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 112,
      "name": "Al-Ikhlas ",
      "start_page": 604,
      "end_page": 604,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 113,
      "name": "Al-Falaq ",
      "start_page": 604,
      "end_page": 604,
      "makkia": 1,
      "type": 0
    },
    {
      "id": 114,
      "name": "An-Nas",
      "start_page": 604,
      "end_page": 604,
      "makkia": 1,
      "type": 0
    }
  ]
ar_mohafs = [
    {
      "id": 11,
      "moshaf_type": 1,
      "moshaf_id": 1,
      "name": "حفص عن عاصم - مرتل"
    },
    {
      "id": 12,
      "moshaf_type": 1,
      "moshaf_id": 2,
      "name": "حفص عن عاصم - المصحف المجود"
    },
    {
      "id": 13,
      "moshaf_type": 1,
      "moshaf_id": 3,
      "name": "حفص عن عاصم - المصحف المعلم"
    },
    {
      "id": 21,
      "moshaf_type": 2,
      "moshaf_id": 1,
      "name": "ورش عن نافع - مرتل"
    },
    {
      "id": 31,
      "moshaf_type": 3,
      "moshaf_id": 1,
      "name": "خلف عن حمزة - مرتل"
    },
    {
      "id": 41,
      "moshaf_type": 4,
      "moshaf_id": 1,
      "name": "البزي عن ابن كثير - مرتل"
    },
    {
      "id": 51,
      "moshaf_type": 5,
      "moshaf_id": 1,
      "name": "قالون عن نافع - مرتل"
    },
    {
      "id": 52,
      "moshaf_type": 5,
      "moshaf_id": 2,
      "name": "قالون عن نافع - المصحف المجود"
    },
    {
      "id": 61,
      "moshaf_type": 6,
      "moshaf_id": 1,
      "name": "قنبل عن ابن كثير - مرتل"
    },
    {
      "id": 71,
      "moshaf_type": 7,
      "moshaf_id": 1,
      "name": "السوسي عن أبي عمرو - مرتل"
    },
    {
      "id": 81,
      "moshaf_type": 8,
      "moshaf_id": 1,
      "name": "قالون عن نافع من طريق أبي نشيط - مرتل"
    },
    {
      "id": 91,
      "moshaf_type": 9,
      "moshaf_id": 1,
      "name": "قراءة يعقوب الحضرمي بروايتي رويس وروح - مرتل"
    },
    {
      "id": 101,
      "moshaf_type": 10,
      "moshaf_id": 1,
      "name": "ورش عن نافع من طريق أبي بكر الأصبهاني - مرتل"
    },
    {
      "id": 111,
      "moshaf_type": 11,
      "moshaf_id": 1,
      "name": "البزي وقنبل عن ابن كثير - مرتل"
    },
    {
      "id": 121,
      "moshaf_type": 12,
      "moshaf_id": 1,
      "name": "الدوري عن الكسائي - مرتل"
    },
    {
      "id": 131,
      "moshaf_type": 13,
      "moshaf_id": 1,
      "name": "الدوري عن أبي عمرو - مرتل"
    },
    {
      "id": 132,
      "moshaf_type": 13,
      "moshaf_id": 2,
      "name": "الدوري عن أبي عمرو - المصحف المجود"
    },
    {
      "id": 151,
      "moshaf_type": 15,
      "moshaf_id": 1,
      "name": "شعبة  عن عاصم - مرتل"
    },
    {
      "id": 152,
      "moshaf_type": 15,
      "moshaf_id": 2,
      "name": "شعبة  عن عاصم - المصحف المجود"
    },
    {
      "id": 161,
      "moshaf_type": 16,
      "moshaf_id": 1,
      "name": "ابن ذكوان عن ابن عامر - مرتل"
    },
    {
      "id": 181,
      "moshaf_type": 18,
      "moshaf_id": 1,
      "name": "ورش عن نافع من طريق الأزرق - مرتل"
    },
    {
      "id": 191,
      "moshaf_type": 19,
      "moshaf_id": 1,
      "name": "هشام عن ابي عامر - مرتل"
    },
    {
      "id": 201,
      "moshaf_type": 20,
      "moshaf_id": 1,
      "name": "ابن جماز عن أبي جعفر - مرتل"
    },
    {
      "id": 213,
      "moshaf_type": 21,
      "moshaf_id": 3,
      "name": "المصحف المعلم - المصحف المعلم"
    },
    {
      "id": 222,
      "moshaf_type": 22,
      "moshaf_id": 2,
      "name": "المصحف المجود - المصحف المجود"
    }
  ]
en_mohafs = [
    {
      "id": 11,
      "moshaf_type": 1,
      "moshaf_id": 1,
      "name": "Rewayat Hafs A'n Assem - Murattal"
    },
    {
      "id": 12,
      "moshaf_type": 1,
      "moshaf_id": 2,
      "name": "Rewayat Hafs A'n Assem - Almusshaf Al Mojawwad"
    },
    {
      "id": 13,
      "moshaf_type": 1,
      "moshaf_id": 3,
      "name": "Rewayat Hafs A'n Assem - Almusshaf Al Mo'lim"
    },
    {
      "id": 21,
      "moshaf_type": 2,
      "moshaf_id": 1,
      "name": "Rewayat Warsh A'n Nafi' - Murattal"
    },
    {
      "id": 31,
      "moshaf_type": 3,
      "moshaf_id": 1,
      "name": "Rewayat Khalaf A'n Hamzah - Murattal"
    },
    {
      "id": 41,
      "moshaf_type": 4,
      "moshaf_id": 1,
      "name": "Rewayat Albizi A'n Ibn Katheer - Murattal"
    },
    {
      "id": 51,
      "moshaf_type": 5,
      "moshaf_id": 1,
      "name": "Rewayat Qalon A'n Nafi' - Murattal"
    },
    {
      "id": 52,
      "moshaf_type": 5,
      "moshaf_id": 2,
      "name": "Rewayat Qalon A'n Nafi' - Almusshaf Al Mojawwad"
    },
    {
      "id": 61,
      "moshaf_type": 6,
      "moshaf_id": 1,
      "name": "Rewayat Qunbol A'n Ibn Katheer - Murattal"
    },
    {
      "id": 71,
      "moshaf_type": 7,
      "moshaf_id": 1,
      "name": "Rewayat Assosi A'n Abi Amr - Murattal"
    },
    {
      "id": 81,
      "moshaf_type": 8,
      "moshaf_id": 1,
      "name": "Rewayat Qalon A'n Nafi' Men Tariq Abi Nasheet - Murattal"
    },
    {
      "id": 91,
      "moshaf_type": 9,
      "moshaf_id": 1,
      "name": "Rewayat Rowis and Rawh A'n Yakoob Al Hadrami  - Murattal"
    },
    {
      "id": 101,
      "moshaf_type": 10,
      "moshaf_id": 1,
      "name": "Rewayat Warsh A'n Nafi' Men  Tariq Abi Baker Alasbahani - Murattal"
    },
    {
      "id": 111,
      "moshaf_type": 11,
      "moshaf_id": 1,
      "name": "Rewayat Albizi and Qunbol A'n Ibn Katheer - Murattal"
    },
    {
      "id": 121,
      "moshaf_type": 12,
      "moshaf_id": 1,
      "name": "Rewayat AlDorai A'n Al-Kisa'ai - Murattal"
    },
    {
      "id": 131,
      "moshaf_type": 13,
      "moshaf_id": 1,
      "name": "Rewayat Aldori A'n Abi Amr - Murattal"
    },
    {
      "id": 132,
      "moshaf_type": 13,
      "moshaf_id": 2,
      "name": "Rewayat Aldori A'n Abi Amr - Almusshaf Al Mojawwad"
    },
    {
      "id": 151,
      "moshaf_type": 15,
      "moshaf_id": 1,
      "name": "Sho'bah A'n Asim - Murattal"
    },
    {
      "id": 152,
      "moshaf_type": 15,
      "moshaf_id": 2,
      "name": "Sho'bah A'n Asim - Almusshaf Al Mojawwad"
    },
    {
      "id": 161,
      "moshaf_type": 16,
      "moshaf_id": 1,
      "name": "Ibn Thakwan A'n Ibn Amer - Murattal"
    },
    {
      "id": 181,
      "moshaf_type": 18,
      "moshaf_id": 1,
      "name": "Rewayat Warsh A'n Nafi' Men Tariq Alazraq - Murattal"
    },
    {
      "id": 191,
      "moshaf_type": 19,
      "moshaf_id": 1,
      "name": "Hesham A'n Abi A'mer - Murattal"
    },
    {
      "id": 201,
      "moshaf_type": 20,
      "moshaf_id": 1,
      "name": "Ibn Jammaz A'n Abi Ja'far - Murattal"
    },
    {
      "id": 213,
      "moshaf_type": 21,
      "moshaf_id": 3,
      "name": "Almusshaf Al Mo'lim - Almusshaf Al Mo'lim"
    },
    {
      "id": 222,
      "moshaf_type": 22,
      "moshaf_id": 2,
      "name": "Almusshaf Al Mojawwad - Almusshaf Al Mojawwad"
    }
  ]
ar_reciters = [
    {
      "id": 1,
      "name": "إبراهيم الأخضر",
      "letter": "إ",
      "date": "2020-04-07T02:17:26.000000Z",
      "moshaf": [
        {
          "id": 1,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/akdr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 10,
      "name": "أكرم العلاقمي",
      "letter": "أ",
      "date": "2020-04-07T02:17:28.000000Z",
      "moshaf": [
        {
          "id": 10,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/akrm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 100,
      "name": "ماجد العنزي",
      "letter": "م",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 100,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/majd_onazi/",
          "surah_total": 69,
          "moshaf_type": 11,
          "surah_list": "1,13,14,17,18,19,30,31,32,34,43,44,45,49,50,51,53,55,56,59,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 101,
      "name": "مالك شيبة الحمد",
      "letter": "م",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 101,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/shaibat/",
          "surah_total": 37,
          "moshaf_type": 11,
          "surah_list": "78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 102,
      "name": "ماهر المعيقلي",
      "letter": "م",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 133,
          "name": "المصحف المجود - المصحف المجود",
          "server": "https://server12.mp3quran.net/maher/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 103,
          "name": "المصحف المعلم - المصحف المعلم",
          "server": "https://server12.mp3quran.net/maher/Almusshaf-Al-Mo-lim/",
          "surah_total": 38,
          "moshaf_type": 213,
          "surah_list": "1,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 102,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/maher/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 104,
      "name": "محمد الأيراوي",
      "letter": "م",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 104,
          "name": "ورش عن نافع من طريق الأزرق - مرتل",
          "server": "https://server6.mp3quran.net/earawi/",
          "surah_total": 112,
          "moshaf_type": 181,
          "surah_list": "1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 105,
      "name": "محمد البراك",
      "letter": "م",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 105,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server13.mp3quran.net/braak/",
          "surah_total": 62,
          "moshaf_type": 11,
          "surah_list": "1,12,36,37,44,45,50,51,52,53,54,55,56,57,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 106,
      "name": "محمد الطبلاوي",
      "letter": "م",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 106,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/tblawi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 107,
      "name": "محمد اللحيدان",
      "letter": "م",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 107,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/lhdan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 108,
      "name": "محمد المحيسني",
      "letter": "م",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 108,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/mhsny/",
          "surah_total": 113,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 109,
      "name": "محمد أيوب",
      "letter": "م",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 320,
          "name": "حفص عن عاصم - 4",
          "server": "https://server16.mp3quran.net/ayyoub2/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 14,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 109,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/ayyub/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 11,
      "name": "الحسيني العزازي",
      "letter": "ا",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 11,
          "name": "المصحف المعلم - المصحف المعلم",
          "server": "https://server8.mp3quran.net/3zazi/",
          "surah_total": 57,
          "moshaf_type": 213,
          "surah_list": "58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 110,
      "name": "محمد صالح عالم شاه",
      "letter": "م",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 110,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/shah/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 111,
      "name": "محمد جبريل",
      "letter": "م",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 111,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/jbrl/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 112,
      "name": "محمد صديق المنشاوي",
      "letter": "م",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 114,
          "name": "المصحف المعلم - المصحف المعلم",
          "server": "https://server10.mp3quran.net/minsh/Almusshaf-Al-Mo-lim/",
          "surah_total": 114,
          "moshaf_type": 213,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 113,
          "name": "المصحف المجود - المصحف المجود",
          "server": "https://server10.mp3quran.net/minsh/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 112,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/minsh/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 115,
      "name": "محمد عبدالكريم",
      "letter": "م",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 210,
          "name": "ورش عن نافع من طريق أبي بكر الأصبهاني - مرتل",
          "server": "https://server12.mp3quran.net/m_krm/Rewayat-Warsh-A-n-Nafi-Men-Tariq-Abi-Baker-Alasbahani/",
          "surah_total": 114,
          "moshaf_type": 101,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 115,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/m_krm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 116,
      "name": "محمد عبدالحكيم سعيد العبدالله",
      "letter": "م",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 117,
          "name": "الدوري عن الكسائي - مرتل",
          "server": "https://server9.mp3quran.net/abdullah/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 114,
          "moshaf_type": 121,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 116,
          "name": "البزي وقنبل عن ابن كثير - مرتل",
          "server": "https://server9.mp3quran.net/abdullah/",
          "surah_total": 114,
          "moshaf_type": 111,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 118,
      "name": "محمود خليل الحصري",
      "letter": "م",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 270,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server13.mp3quran.net/husr/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 269,
          "name": "الدوري عن أبي عمرو - مرتل",
          "server": "https://server13.mp3quran.net/husr/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 120,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server13.mp3quran.net/husr/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 119,
          "name": "المصحف المجود - المصحف المجود",
          "server": "https://server13.mp3quran.net/husr/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 118,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server13.mp3quran.net/husr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 12,
      "name": "إدريس أبكر",
      "letter": "إ",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 12,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/abkr/",
          "surah_total": 111,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 121,
      "name": "محمود علي البنا",
      "letter": "م",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 122,
          "name": "المصحف المجود - المصحف المجود",
          "server": "https://server8.mp3quran.net/bna/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 121,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/bna/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 123,
      "name": "مشاري العفاسي",
      "letter": "م",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 124,
          "name": "الدوري عن الكسائي - مرتل",
          "server": "https://server8.mp3quran.net/afs/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 5,
          "moshaf_type": 121,
          "surah_list": "14,25,87,97,99"
        },
        {
          "id": 123,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/afs/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 125,
      "name": "مصطفى إسماعيل",
      "letter": "م",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 288,
          "name": "المصحف المجود - المصحف المجود",
          "server": "https://server8.mp3quran.net/mustafa/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 125,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/mustafa/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 126,
      "name": "مصطفى اللاهوني",
      "letter": "م",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 126,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/lahoni/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 127,
      "name": "مصطفى رعد العزاوي",
      "letter": "م",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 127,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/ra3ad/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 128,
      "name": "معمر الأندونيسي",
      "letter": "م",
      "date": "2020-04-07T02:17:54.000000Z",
      "moshaf": [
        {
          "id": 128,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/muamr/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "36,93,94,97,101,109,110,111"
        }
      ]
    },
    {
      "id": 129,
      "name": "مفتاح السلطني",
      "letter": "م",
      "date": "2024-04-22T22:29:17.000000Z",
      "moshaf": [
        {
          "id": 196,
          "name": "ابن ذكوان عن ابن عامر - مرتل",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat_Ibn-Thakwan-A-n-Ibn-Amer/",
          "surah_total": 114,
          "moshaf_type": 161,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 195,
          "name": "شعبة  عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat_Sho-bah-A-n-Asim/",
          "surah_total": 77,
          "moshaf_type": 151,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77"
        },
        {
          "id": 182,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 180,
          "name": "الدوري عن الكسائي - مرتل",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 114,
          "moshaf_type": 121,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 129,
          "name": "الدوري عن أبي عمرو - مرتل",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 13,
      "name": "الزين محمد أحمد",
      "letter": "ا",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 13,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/alzain/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 134,
      "name": "محمد سايد",
      "letter": "م",
      "date": "2021-05-06T11:13:52.000000Z",
      "moshaf": [
        {
          "id": 134,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/m_sayed/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 135,
      "name": "عبدالرحمن السويّد",
      "letter": "ع",
      "date": "2021-05-19T14:25:00.000000Z",
      "moshaf": [
        {
          "id": 135,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_swaiyd/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 85,
          "moshaf_type": 11,
          "surah_list": "2,11,15,18,19,25,34,35,36,37,38,39,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 136,
      "name": "عبدالإله بن عون",
      "letter": "ع",
      "date": "2021-05-20T13:46:47.000000Z",
      "moshaf": [
        {
          "id": 136,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_binaoun/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 137,
      "name": "أحمد طالب بن حميد",
      "letter": "أ",
      "date": "2021-05-29T16:44:43.000000Z",
      "moshaf": [
        {
          "id": 137,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_binhameed/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 82,
          "moshaf_type": 11,
          "surah_list": "1,2,5,6,8,10,12,18,20,29,30,31,32,35,37,38,44,45,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 138,
      "name": "نورين محمد صديق",
      "letter": "ن",
      "date": "2021-06-29T11:08:49.000000Z",
      "moshaf": [
        {
          "id": 138,
          "name": "الدوري عن أبي عمرو - مرتل",
          "server": "https://server16.mp3quran.net/nourin_siddig/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 139,
      "name": "ماجد الزامل",
      "letter": "م",
      "date": "2020-04-07T02:17:54.000000Z",
      "moshaf": [
        {
          "id": 139,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/zaml/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 14,
      "name": "القارئ ياسين",
      "letter": "ا",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 14,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server11.mp3quran.net/qari/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 149,
      "name": "ماهر شخاشيرو",
      "letter": "م",
      "date": "2020-04-07T02:17:54.000000Z",
      "moshaf": [
        {
          "id": 149,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/shaksh/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 15,
      "name": "العشري عمران",
      "letter": "ا",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 15,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/omran/",
          "surah_total": 113,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 150,
      "name": "محمد المنشد",
      "letter": "م",
      "date": "2020-04-07T02:17:55.000000Z",
      "moshaf": [
        {
          "id": 150,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/monshed/",
          "surah_total": 110,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 151,
      "name": "محمود الشيمي",
      "letter": "م",
      "date": "2020-04-07T02:17:55.000000Z",
      "moshaf": [
        {
          "id": 151,
          "name": "الدوري عن الكسائي - مرتل",
          "server": "https://server10.mp3quran.net/sheimy/",
          "surah_total": 114,
          "moshaf_type": 121,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 152,
      "name": "ياسر سلامة",
      "letter": "ي",
      "date": "2020-04-07T02:17:55.000000Z",
      "moshaf": [
        {
          "id": 152,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/salamah/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 153,
      "name": "أخيل عبدالحي روا",
      "letter": "أ",
      "date": "2022-06-23T10:49:15.000000Z",
      "moshaf": [
        {
          "id": 153,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/akil/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "50,51,52,56"
        }
      ]
    },
    {
      "id": 154,
      "name": "أستاذ زامري",
      "letter": "أ",
      "date": "2022-06-23T10:49:03.000000Z",
      "moshaf": [
        {
          "id": 154,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/zamri/",
          "surah_total": 7,
          "moshaf_type": 11,
          "surah_list": "32,44,55,56,61,67,76"
        }
      ]
    },
    {
      "id": 159,
      "name": "خالد المهنا",
      "letter": "خ",
      "date": "2020-04-07T02:17:56.000000Z",
      "moshaf": [
        {
          "id": 159,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/mohna/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 16,
      "name": "العيون الكوشي",
      "letter": "ا",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 16,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server11.mp3quran.net/koshi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 160,
      "name": "عادل الكلباني",
      "letter": "ع",
      "date": "2020-04-07T02:17:56.000000Z",
      "moshaf": [
        {
          "id": 160,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/a_klb/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 161,
      "name": "موسى بلال",
      "letter": "م",
      "date": "2020-04-07T02:17:56.000000Z",
      "moshaf": [
        {
          "id": 161,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/bilal/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 162,
      "name": "حسين آل الشيخ",
      "letter": "ح",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 162,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/alshaik/",
          "surah_total": 15,
          "moshaf_type": 11,
          "surah_list": "13,14,22,32,38,44,45,49,50,78,79,80,81,82,85"
        }
      ]
    },
    {
      "id": 163,
      "name": "حاتم فريد الواعر",
      "letter": "ح",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 163,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/hatem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 164,
      "name": "إبراهيم الجرمي",
      "letter": "إ",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 164,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/jormy/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 165,
      "name": "محمود الرفاعي",
      "letter": "م",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 165,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/mrifai/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 166,
      "name": "ناصر العبيد",
      "letter": "ن",
      "date": "2020-04-07T02:17:58.000000Z",
      "moshaf": [
        {
          "id": 166,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/obaid/",
          "surah_total": 9,
          "moshaf_type": 11,
          "surah_list": "7,13,14,15,25,26,27,40,41"
        }
      ]
    },
    {
      "id": 167,
      "name": "واصل المذن",
      "letter": "و",
      "date": "2020-04-07T02:17:58.000000Z",
      "moshaf": [
        {
          "id": 167,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/wasel/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 9,
          "moshaf_type": 11,
          "surah_list": "8,9,36,38,42,45,50,59,60"
        }
      ]
    },
    {
      "id": 17,
      "name": "توفيق الصايغ",
      "letter": "ت",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 17,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/twfeeq/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 178,
      "name": "إبراهيم الدوسري",
      "letter": "إ",
      "date": "2022-06-23T10:51:41.000000Z",
      "moshaf": [
        {
          "id": 232,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/ibrahim_dosri/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 178,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server10.mp3quran.net/ibrahim_dosri/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 18,
      "name": "جمال شاكر عبدالله",
      "letter": "ج",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 18,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/jamal/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 181,
      "name": "جمعان العصيمي",
      "letter": "ج",
      "date": "2020-04-07T02:17:58.000000Z",
      "moshaf": [
        {
          "id": 181,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/jaman/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 183,
      "name": "رضية عبدالرحمن",
      "letter": "ر",
      "date": "2022-06-23T10:48:49.000000Z",
      "moshaf": [
        {
          "id": 183,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/rziah/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "3,8,33,35"
        }
      ]
    },
    {
      "id": 184,
      "name": "رقية سولونق",
      "letter": "ر",
      "date": "2022-06-23T10:48:41.000000Z",
      "moshaf": [
        {
          "id": 184,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/rogiah/",
          "surah_total": 1,
          "moshaf_type": 11,
          "surah_list": "36"
        }
      ]
    },
    {
      "id": 185,
      "name": "سابينة مامات",
      "letter": "س",
      "date": "2022-06-23T10:48:31.000000Z",
      "moshaf": [
        {
          "id": 185,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/mamat/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "3,14,21,22"
        }
      ]
    },
    {
      "id": 187,
      "name": "سيدين عبدالرحمن",
      "letter": "س",
      "date": "2022-06-23T10:48:22.000000Z",
      "moshaf": [
        {
          "id": 187,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/sideen/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "17,23,56,75"
        }
      ]
    },
    {
      "id": 188,
      "name": "عبدالغني عبدالله",
      "letter": "ع",
      "date": "2022-06-23T10:48:12.000000Z",
      "moshaf": [
        {
          "id": 188,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/abdulgani/",
          "surah_total": 13,
          "moshaf_type": 11,
          "surah_list": "1,2,5,6,9,67,87,91,92,94,95,97,114"
        }
      ]
    },
    {
      "id": 189,
      "name": "عبدالله فهمي",
      "letter": "ع",
      "date": "2022-06-23T10:48:03.000000Z",
      "moshaf": [
        {
          "id": 189,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/fhmi/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,36,53,75"
        }
      ]
    },
    {
      "id": 19,
      "name": "حمد الدغريري",
      "letter": "ح",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 19,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/hamad/",
          "surah_total": 5,
          "moshaf_type": 11,
          "surah_list": "1,12,13,43,44"
        }
      ]
    },
    {
      "id": 190,
      "name": "محمد الحافظ",
      "letter": "م",
      "date": "2022-06-23T10:47:45.000000Z",
      "moshaf": [
        {
          "id": 190,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/hafz/",
          "surah_total": 3,
          "moshaf_type": 11,
          "surah_list": "1,19,31"
        }
      ]
    },
    {
      "id": 191,
      "name": "محمد حفص علي",
      "letter": "م",
      "date": "2022-06-23T10:47:14.000000Z",
      "moshaf": [
        {
          "id": 191,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/hfs/",
          "surah_total": 5,
          "moshaf_type": 11,
          "surah_list": "1,9,11,13,67"
        }
      ]
    },
    {
      "id": 192,
      "name": "محمد خير النور",
      "letter": "م",
      "date": "2020-10-19T15:36:39.000000Z",
      "moshaf": [
        {
          "id": 192,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/malaysia/nor/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,12,19,31"
        }
      ]
    },
    {
      "id": 193,
      "name": "يوسف بن نوح أحمد",
      "letter": "ي",
      "date": "2020-04-07T02:18:01.000000Z",
      "moshaf": [
        {
          "id": 193,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/noah/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 194,
      "name": "جمال الدين الزيلعي",
      "letter": "ج",
      "date": "2020-04-07T02:18:01.000000Z",
      "moshaf": [
        {
          "id": 194,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/zilaie/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "1,19,32,54,67,70,73,91"
        }
      ]
    },
    {
      "id": 197,
      "name": "معيض الحارثي",
      "letter": "م",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 197,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/harthi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 198,
      "name": "محمد رشاد الشريف",
      "letter": "م",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 198,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/rashad/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 2,
      "name": "إبراهيم الجبرين",
      "letter": "إ",
      "date": "2020-04-07T02:17:26.000000Z",
      "moshaf": [
        {
          "id": 2,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/jbreen/",
          "surah_total": 99,
          "moshaf_type": 11,
          "surah_list": "1,3,4,7,8,10,12,13,14,15,16,17,18,19,20,21,23,25,27,31,32,33,34,36,37,38,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 20,
      "name": "خالد الجليل",
      "letter": "خ",
      "date": "2020-04-07T02:17:31.000000Z",
      "moshaf": [
        {
          "id": 20,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/jleel/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 201,
      "name": "أحمد الطرابلسي",
      "letter": "أ",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 201,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/trabulsi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 199,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server10.mp3quran.net/trablsi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 202,
      "name": "عبدالله الكندري",
      "letter": "ع",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 202,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/Abdullahk/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 203,
      "name": "أحمد عامر",
      "letter": "أ",
      "date": "2020-04-07T02:18:03.000000Z",
      "moshaf": [
        {
          "id": 203,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/Aamer/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 204,
      "name": "إبراهيم السعدان",
      "letter": "إ",
      "date": "2022-06-23T10:50:29.000000Z",
      "moshaf": [
        {
          "id": 204,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/IbrahemSadan/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,6,19,20"
        }
      ]
    },
    {
      "id": 205,
      "name": "أحمد الحذيفي",
      "letter": "أ",
      "date": "2020-04-07T02:18:03.000000Z",
      "moshaf": [
        {
          "id": 205,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/ahmad_huth/",
          "surah_total": 105,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,38,41,42,43,44,45,47,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 206,
      "name": "محمد عثمان خان",
      "letter": "م",
      "date": "2020-06-15T22:08:39.000000Z",
      "moshaf": [
        {
          "id": 206,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/khan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 207,
      "name": "يوسف الدغوش",
      "letter": "ي",
      "date": "2020-06-15T21:51:49.000000Z",
      "moshaf": [
        {
          "id": 207,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server7.mp3quran.net/dgsh/",
          "surah_total": 22,
          "moshaf_type": 11,
          "surah_list": "1,3,55,67,71,75,82,85,90,91,92,100,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 208,
      "name": "الدوكالي محمد العالم",
      "letter": "ا",
      "date": "2020-04-07T02:18:04.000000Z",
      "moshaf": [
        {
          "id": 208,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server7.mp3quran.net/dokali/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 209,
      "name": "وشيار حيدر اربيلي",
      "letter": "و",
      "date": "2020-04-07T02:18:04.000000Z",
      "moshaf": [
        {
          "id": 209,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/wishear/",
          "surah_total": 2,
          "moshaf_type": 11,
          "surah_list": "55,56"
        }
      ]
    },
    {
      "id": 21,
      "name": "خالد القحطاني",
      "letter": "خ",
      "date": "2020-04-07T02:17:31.000000Z",
      "moshaf": [
        {
          "id": 21,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/qht/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 211,
      "name": "الفاتح محمد الزبير",
      "letter": "ا",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 211,
          "name": "الدوري عن أبي عمرو - مرتل",
          "server": "https://server6.mp3quran.net/fateh/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21181,
      "name": "محمد برهجي",
      "letter": "م",
      "date": "2024-03-20T22:13:58.000000Z",
      "moshaf": [
        {
          "id": 340,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/M_Burhaji/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21182,
      "name": "يوسف العيدروس",
      "letter": "ي",
      "date": "2024-09-04T01:26:29.000000Z",
      "moshaf": [
        {
          "id": 10904,
          "name": "حفص عن عاصم - 4",
          "server": "https://server16.mp3quran.net/Y_ALaidroos/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 99,
          "moshaf_type": 14,
          "surah_list": "1,2,3,4,5,7,8,9,10,11,12,14,15,17,18,19,24,26,27,28,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21183,
      "name": "حسن الدغريري",
      "letter": "ح",
      "date": "2024-12-04T16:33:47.000000Z",
      "moshaf": [
        {
          "id": 10905,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/H-Aldaghriri/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21184,
      "name": "محمد الفقيه",
      "letter": "م",
      "date": "2024-12-18T20:27:10.000000Z",
      "moshaf": [
        {
          "id": 10906,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/M_Alfaqih/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21185,
      "name": "أحمد البشر",
      "letter": "أ",
      "date": "2024-12-25T13:47:02.000000Z",
      "moshaf": [
        {
          "id": 10907,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_albishr/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21186,
      "name": "جنيد ادم عبدالله",
      "letter": "ج",
      "date": "2025-02-09T20:21:02.000000Z",
      "moshaf": [
        {
          "id": 10908,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/J-Abdullah/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 212,
      "name": "طارق عبدالغني دعوب",
      "letter": "ط",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 212,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server10.mp3quran.net/tareq/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 216,
      "name": "عثمان الأنصاري",
      "letter": "ع",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 216,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/Othmn/",
          "surah_total": 76,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 217,
      "name": "بندر بليله",
      "letter": "ب",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 217,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/balilah/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 218,
      "name": "خالد الشريمي",
      "letter": "خ",
      "date": "2020-04-07T02:18:06.000000Z",
      "moshaf": [
        {
          "id": 218,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/shoraimy/",
          "surah_total": 73,
          "moshaf_type": 11,
          "surah_list": "1,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 219,
      "name": "وديع اليمني",
      "letter": "و",
      "date": "2020-04-07T02:18:06.000000Z",
      "moshaf": [
        {
          "id": 219,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/wdee3/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 22,
      "name": "خالد عبدالكافي",
      "letter": "خ",
      "date": "2020-04-07T02:17:31.000000Z",
      "moshaf": [
        {
          "id": 22,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/kafi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 221,
      "name": "رعد محمد الكردي",
      "letter": "ر",
      "date": "2020-04-07T02:18:06.000000Z",
      "moshaf": [
        {
          "id": 221,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/kurdi/",
          "surah_total": 93,
          "moshaf_type": 11,
          "surah_list": "1,2,3,12,13,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,35,36,37,38,39,41,42,43,44,46,47,48,51,52,56,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 225,
      "name": "عبدالرحمن العوسي",
      "letter": "ع",
      "date": "2023-10-04T21:50:14.000000Z",
      "moshaf": [
        {
          "id": 225,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/aloosi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 226,
      "name": "خالد الغامدي",
      "letter": "خ",
      "date": "2020-04-07T02:18:07.000000Z",
      "moshaf": [
        {
          "id": 226,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/ghamdi/",
          "surah_total": 28,
          "moshaf_type": 11,
          "surah_list": "1,6,9,14,21,25,30,42,50,52,53,54,58,59,60,61,65,67,68,69,70,71,77,85,86,88,91,93"
        }
      ]
    },
    {
      "id": 227,
      "name": "رمضان شكور",
      "letter": "ر",
      "date": "2020-04-07T02:18:07.000000Z",
      "moshaf": [
        {
          "id": 227,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/shakoor/",
          "surah_total": 61,
          "moshaf_type": 11,
          "surah_list": "1,3,10,13,14,23,26,29,35,36,39,40,42,43,47,48,49,50,51,57,58,59,60,63,68,69,70,71,72,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,114"
        }
      ]
    },
    {
      "id": 228,
      "name": "عبدالمجيد الأركاني",
      "letter": "ع",
      "date": "2020-04-07T02:18:07.000000Z",
      "moshaf": [
        {
          "id": 228,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server7.mp3quran.net/m_arkani/",
          "surah_total": 46,
          "moshaf_type": 11,
          "surah_list": "12,18,19,21,22,40,50,56,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 229,
      "name": "محمد خليل القارئ",
      "letter": "م",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 229,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/m_qari/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 23,
      "name": "خالد الوهيبي",
      "letter": "خ",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 23,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/whabi/",
          "surah_total": 11,
          "moshaf_type": 11,
          "surah_list": "12,13,14,16,19,24,25,29,30,31,32"
        }
      ]
    },
    {
      "id": 230,
      "name": "رامي الدعيس",
      "letter": "ر",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 230,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/rami/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 231,
      "name": "هزاع البلوشي",
      "letter": "ه",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 231,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/hazza/",
          "surah_total": 75,
          "moshaf_type": 11,
          "surah_list": "1,13,14,15,18,19,25,29,30,31,36,37,38,39,40,42,44,47,49,50,51,52,53,54,55,56,57,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 236,
      "name": "عبدالرحمن الماجد",
      "letter": "ع",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 236,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/a_majed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 237,
      "name": "مروان العكري",
      "letter": "م",
      "date": "2022-02-02T17:25:47.000000Z",
      "moshaf": [
        {
          "id": 287,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/m_akri/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 24,
      "name": "خليفة الطنيجي",
      "letter": "خ",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 24,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/tnjy/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 240,
      "name": "سلمان العتيبي",
      "letter": "س",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 240,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/salman/",
          "surah_total": 61,
          "moshaf_type": 11,
          "surah_list": "1,2,36,46,56,58,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 241,
      "name": "محمد رفعت",
      "letter": "م",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 241,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/refat/",
          "surah_total": 31,
          "moshaf_type": 11,
          "surah_list": "1,10,11,12,17,18,19,20,48,54,55,56,69,72,73,75,76,77,78,79,81,82,83,85,86,87,88,89,96,98,100"
        }
      ]
    },
    {
      "id": 243,
      "name": "عبدالله الموسى",
      "letter": "ع",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 286,
          "name": "المصحف المعلم - المصحف المعلم",
          "server": "https://server14.mp3quran.net/mousa/Almusshaf-Al-Mo-lim/",
          "surah_total": 38,
          "moshaf_type": 213,
          "surah_list": "1,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 243,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/mousa/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 102,
          "moshaf_type": 11,
          "surah_list": "1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,29,31,32,33,35,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 244,
      "name": "عبدالله الخلف",
      "letter": "ع",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 244,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/khalf/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 245,
      "name": "منصور السالمي",
      "letter": "م",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 245,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/mansor/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 246,
      "name": "صلاح مصلي",
      "letter": "ص",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 246,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/musali/",
          "surah_total": 48,
          "moshaf_type": 11,
          "surah_list": "67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 247,
      "name": "خالد الشارخ",
      "letter": "خ",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 247,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/sharekh/",
          "surah_total": 64,
          "moshaf_type": 11,
          "surah_list": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 248,
      "name": "ناصر العصفور",
      "letter": "ن",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 248,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/alosfor/",
          "surah_total": 111,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 25,
      "name": "داود حمزة",
      "letter": "د",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 25,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/hamza/",
          "surah_total": 86,
          "moshaf_type": 11,
          "surah_list": "2,3,5,6,7,8,10,12,14,16,17,18,19,20,21,23,24,25,27,28,29,31,33,34,35,36,37,38,40,41,42,46,47,48,50,52,53,54,56,58,60,61,63,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,96,97,98,101,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 250,
      "name": "محمد البخيت",
      "letter": "م",
      "date": "2020-04-07T02:18:14.000000Z",
      "moshaf": [
        {
          "id": 250,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/bukheet/",
          "surah_total": 109,
          "moshaf_type": 11,
          "surah_list": "1,2,3,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 251,
      "name": "ناصر الماجد",
      "letter": "ن",
      "date": "2020-04-07T02:18:13.000000Z",
      "moshaf": [
        {
          "id": 251,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/nasser_almajed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 252,
      "name": "أحمد السويلم",
      "letter": "أ",
      "date": "2020-04-07T02:18:11.000000Z",
      "moshaf": [
        {
          "id": 252,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/swlim/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 253,
      "name": "إسلام صبحي",
      "letter": "إ",
      "date": "2020-04-07T02:18:12.000000Z",
      "moshaf": [
        {
          "id": 253,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server14.mp3quran.net/islam/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 93,
          "moshaf_type": 11,
          "surah_list": "1,2,5,11,12,13,14,15,17,18,19,20,21,23,24,25,26,27,29,30,31,32,34,35,36,38,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,111,114"
        }
      ]
    },
    {
      "id": 254,
      "name": "بدر التركي",
      "letter": "ب",
      "date": "2020-04-07T02:18:12.000000Z",
      "moshaf": [
        {
          "id": 254,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/bader/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 255,
      "name": "هيثم الجدعاني",
      "letter": "ه",
      "date": "2020-04-07T02:18:13.000000Z",
      "moshaf": [
        {
          "id": 255,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/hitham/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 38,
          "moshaf_type": 11,
          "surah_list": "1,2,6,7,8,9,10,12,13,14,15,16,28,29,30,31,32,34,35,36,37,38,44,50,51,52,53,54,55,56,57,69,75,76,85,87,88,90"
        }
      ]
    },
    {
      "id": 256,
      "name": "أحمد خليل شاهين",
      "letter": "أ",
      "date": "2020-04-07T02:18:13.000000Z",
      "moshaf": [
        {
          "id": 256,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/shaheen/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 257,
      "name": "سعد المقرن",
      "letter": "س",
      "date": "2020-04-07T02:18:14.000000Z",
      "moshaf": [
        {
          "id": 257,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/saad/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 259,
      "name": "أحمد النفيس",
      "letter": "أ",
      "date": "2023-01-30T15:24:51.000000Z",
      "moshaf": [
        {
          "id": 259,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/nufais/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 26,
      "name": "رشيد إفراد",
      "letter": "ر",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 26,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server12.mp3quran.net/ifrad/",
          "surah_total": 15,
          "moshaf_type": 21,
          "surah_list": "1,18,25,26,27,28,29,31,33,35,37,38,41,42,71"
        }
      ]
    },
    {
      "id": 260,
      "name": "عمر الدريويز",
      "letter": "ع",
      "date": "2020-05-04T22:45:38.000000Z",
      "moshaf": [
        {
          "id": 260,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/darweez/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 61,
          "moshaf_type": 11,
          "surah_list": "1,12,13,15,18,19,25,32,36,38,44,47,48,50,51,52,53,54,56,61,62,63,64,66,67,68,70,71,72,73,74,75,76,78,79,80,82,85,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 263,
      "name": "عبدالعزيز العسيري",
      "letter": "ع",
      "date": "2020-05-04T23:43:58.000000Z",
      "moshaf": [
        {
          "id": 263,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/abdulazizasiri/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 21,
          "moshaf_type": 11,
          "surah_list": "2,3,5,11,12,13,14,17,18,36,45,51,55,57,67,70,71,73,78,86,88"
        }
      ]
    },
    {
      "id": 264,
      "name": "يونس اسويلص",
      "letter": "ي",
      "date": "2020-05-25T18:13:32.000000Z",
      "moshaf": [
        {
          "id": 264,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/souilass/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 13,
          "moshaf_type": 21,
          "surah_list": "1,18,19,25,50,51,56,57,67,73,91,97,112"
        }
      ]
    },
    {
      "id": 265,
      "name": "أحمد ديبان",
      "letter": "أ",
      "date": "2020-06-16T22:06:00.000000Z",
      "moshaf": [
        {
          "id": 313,
          "name": "ابن جماز عن أبي جعفر - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Ibn-Jammaz-A-n-Abi-Ja-far/",
          "surah_total": 11,
          "moshaf_type": 201,
          "surah_list": "1,93,100,102,103,109,110,111,112,113,114"
        },
        {
          "id": 312,
          "name": "هشام عن ابي عامر - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Hesham-A-n-Abi-A-mer/",
          "surah_total": 27,
          "moshaf_type": 191,
          "surah_list": "1,2,3,4,5,6,7,8,9,13,85,90,92,93,94,95,99,100,101,103,105,107,108,110,112,113,114"
        },
        {
          "id": 311,
          "name": "خلف عن حمزة - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Khalaf-A-n-Hamzah/",
          "surah_total": 6,
          "moshaf_type": 31,
          "surah_list": "94,97,101,107,108,109"
        },
        {
          "id": 310,
          "name": "الدوري عن الكسائي - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 13,
          "moshaf_type": 121,
          "surah_list": "1,94,95,100,103,105,106,108,109,110,112,113,114"
        },
        {
          "id": 309,
          "name": "السوسي عن أبي عمرو - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Assosi-A-n-Abi-Amr/",
          "surah_total": 19,
          "moshaf_type": 71,
          "surah_list": "1,82,86,87,88,93,94,95,99,102,103,106,108,109,110,111,112,113,114"
        },
        {
          "id": 308,
          "name": "ابن ذكوان عن ابن عامر - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Ibn-Thakwan-A-n-Ibn-Amer/",
          "surah_total": 33,
          "moshaf_type": 161,
          "surah_list": "1,2,3,4,5,6,7,8,9,13,77,83,85,86,88,90,92,93,94,95,96,97,99,100,101,103,105,107,108,109,112,113,114"
        },
        {
          "id": 301,
          "name": "ورش عن نافع من طريق الأزرق - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Warsh-A-n-Nafi-Men-Tariq-Alazraq/",
          "surah_total": 114,
          "moshaf_type": 181,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 285,
          "name": "الدوري عن أبي عمرو - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 280,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 279,
          "name": "البزي عن ابن كثير - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Albizi-A-n-Ibn-Katheer/",
          "surah_total": 114,
          "moshaf_type": 41,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 278,
          "name": "قنبل عن ابن كثير - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Qunbol-A-n-Ibn-Katheer/",
          "surah_total": 114,
          "moshaf_type": 61,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 276,
          "name": "شعبة  عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Sho-bah-A-n-Asim/",
          "surah_total": 114,
          "moshaf_type": 151,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 265,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 267,
      "name": "عبدالله كامل",
      "letter": "ع",
      "date": "2020-06-30T21:09:29.000000Z",
      "moshaf": [
        {
          "id": 267,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/kamel/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 268,
      "name": "بيشه وا قادر الكردي",
      "letter": "ب",
      "date": "2020-07-05T10:15:00.000000Z",
      "moshaf": [
        {
          "id": 268,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/peshawa/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 27,
      "name": "رشيد بلعالية",
      "letter": "ر",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 261,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/bl3/",
          "surah_total": 5,
          "moshaf_type": 11,
          "surah_list": "46,47,48,49,50"
        },
        {
          "id": 27,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server6.mp3quran.net/bl3/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 271,
      "name": "نذير المالكي",
      "letter": "ن",
      "date": "2020-07-17T17:01:21.000000Z",
      "moshaf": [
        {
          "id": 271,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net//nathier/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 272,
      "name": "عكاشة كميني",
      "letter": "ع",
      "date": "2021-01-24T20:32:19.000000Z",
      "moshaf": [
        {
          "id": 296,
          "name": "البزي عن ابن كثير - مرتل",
          "server": "https://server16.mp3quran.net/okasha/Rewayat-Albizi-A-n-Ibn-Katheer/",
          "surah_total": 114,
          "moshaf_type": 41,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 272,
          "name": "الدوري عن الكسائي - مرتل",
          "server": "https://server16.mp3quran.net/okasha/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 38,
          "moshaf_type": 121,
          "surah_list": "17,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 273,
      "name": "هيثم الدخين",
      "letter": "ه",
      "date": "2021-03-25T13:38:35.000000Z",
      "moshaf": [
        {
          "id": 273,
          "name": "حفص عن عاصم - 4",
          "server": "https://server16.mp3quran.net/h_dukhain/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 14,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 274,
      "name": "محمد أبو سنينة",
      "letter": "م",
      "date": "2021-03-16T19:38:11.000000Z",
      "moshaf": [
        {
          "id": 274,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/sneineh/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 275,
      "name": "محمد الأمين قنيوة",
      "letter": "م",
      "date": "2021-03-18T18:20:44.000000Z",
      "moshaf": [
        {
          "id": 275,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/qeniwa/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 277,
      "name": "محمود عبدالحكم",
      "letter": "م",
      "date": "2021-04-24T20:07:17.000000Z",
      "moshaf": [
        {
          "id": 277,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/m_abdelhakam/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 113,
          "moshaf_type": 11,
          "surah_list": "1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 278,
      "name": "أحمد عيسى المعصراوي",
      "letter": "أ",
      "date": "2022-05-16T19:26:36.000000Z",
      "moshaf": [
        {
          "id": 290,
          "name": "قراءة يعقوب الحضرمي بروايتي رويس وروح - مرتل",
          "server": "https://server16.mp3quran.net/a_maasaraawi/Rewayat-Rawh-A-n-Yakoob-Alhadrami/",
          "surah_total": 64,
          "moshaf_type": 91,
          "surah_list": "51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 289,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_maasaraawi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 279,
      "name": "إبراهيم كشيدان",
      "letter": "إ",
      "date": "2022-05-23T18:43:01.000000Z",
      "moshaf": [
        {
          "id": 291,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/i_kshidan/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 28,
      "name": "زكريا حمامة",
      "letter": "ز",
      "date": "2020-04-07T02:17:33.000000Z",
      "moshaf": [
        {
          "id": 28,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/zakariya/",
          "surah_total": 7,
          "moshaf_type": 11,
          "surah_list": "32,36,44,56,67,76,85"
        }
      ]
    },
    {
      "id": 280,
      "name": "هاشم أبو دلال",
      "letter": "ه",
      "date": "2022-05-25T14:25:53.000000Z",
      "moshaf": [
        {
          "id": 292,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/h_abudalal/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 281,
      "name": "فؤاد الخامري",
      "letter": "ف",
      "date": "2022-05-26T13:35:45.000000Z",
      "moshaf": [
        {
          "id": 293,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/f_khamery/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 282,
      "name": "سيد أحمد هاشمي",
      "letter": "س",
      "date": "2022-06-09T13:21:46.000000Z",
      "moshaf": [
        {
          "id": 294,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/s_hashemi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 283,
      "name": "خالد كريم محمدي",
      "letter": "خ",
      "date": "2022-06-09T13:40:21.000000Z",
      "moshaf": [
        {
          "id": 295,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/kh_mohammadi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 284,
      "name": "مال الله عبدالرحمن الجابر",
      "letter": "م",
      "date": "2022-08-11T10:41:02.000000Z",
      "moshaf": [
        {
          "id": 297,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/mal-allah_jaber/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 285,
      "name": "سلمان الصديق",
      "letter": "س",
      "date": "2022-08-11T13:53:11.000000Z",
      "moshaf": [
        {
          "id": 298,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/s_sadeiq/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 286,
      "name": "حسن صالح",
      "letter": "ح",
      "date": "2022-08-16T10:28:32.000000Z",
      "moshaf": [
        {
          "id": 299,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/h_saleh/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 287,
      "name": "عبدالرحمن الشحات",
      "letter": "ع",
      "date": "2022-09-02T17:28:53.000000Z",
      "moshaf": [
        {
          "id": 302,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_alshahhat/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 288,
      "name": "عيسى عمر سناكو",
      "letter": "ع",
      "date": "2022-09-10T19:21:58.000000Z",
      "moshaf": [
        {
          "id": 303,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/i_sanankoua/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 26,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,6,12,14,18,20,32,35,40,50,56,57,58,63,67,71,78,87,88,91,112,113,114"
        }
      ]
    },
    {
      "id": 289,
      "name": "هارون بقائي",
      "letter": "ه",
      "date": "2022-11-23T15:10:37.000000Z",
      "moshaf": [
        {
          "id": 304,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/h_baqai/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 51,
          "moshaf_type": 11,
          "surah_list": "1,56,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 29,
      "name": "عبدالله بخاري",
      "letter": "ع",
      "date": "2021-09-17T17:46:33.000000Z",
      "moshaf": [
        {
          "id": 281,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_bukhari/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 80,
          "moshaf_type": 11,
          "surah_list": "1,2,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 290,
      "name": "صالح القريشي",
      "letter": "ص",
      "date": "2023-10-17T21:16:11.000000Z",
      "moshaf": [
        {
          "id": 306,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/s_alquraishi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 3,
      "name": "إبراهيم العسيري",
      "letter": "إ",
      "date": "2020-04-07T02:17:26.000000Z",
      "moshaf": [
        {
          "id": 3,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/3siri/",
          "surah_total": 27,
          "moshaf_type": 11,
          "surah_list": "1,3,4,5,8,12,13,14,17,18,19,20,21,23,27,34,36,38,51,53,54,56,67,69,70,75,76"
        }
      ]
    },
    {
      "id": 30,
      "name": "سعد الغامدي",
      "letter": "س",
      "date": "2020-04-07T02:17:33.000000Z",
      "moshaf": [
        {
          "id": 30,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server7.mp3quran.net/s_gmd/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 300,
      "name": "صالح الشمراني",
      "letter": "ص",
      "date": "2022-06-26T19:29:02.000000Z",
      "moshaf": [
        {
          "id": 300,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/shamrani/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 301,
      "name": "فيصل الهاجري",
      "letter": "ف",
      "date": "2023-01-29T19:24:52.000000Z",
      "moshaf": [
        {
          "id": 307,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/f_hajry/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 302,
      "name": "أنس العمادي",
      "letter": "أ",
      "date": "2023-03-29T20:25:16.000000Z",
      "moshaf": [
        {
          "id": 314,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_alemadi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 303,
      "name": "عبدالملك العسكر",
      "letter": "ع",
      "date": "2023-04-05T16:21:27.000000Z",
      "moshaf": [
        {
          "id": 315,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_alaskar/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 6,
          "moshaf_type": 11,
          "surah_list": "36,40,69,70,71,75"
        }
      ]
    },
    {
      "id": 304,
      "name": "عبدالكريم الحازمي",
      "letter": "ع",
      "date": "2023-08-12T16:44:36.000000Z",
      "moshaf": [
        {
          "id": 316,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_alhazmi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 305,
      "name": "هشام الهراز",
      "letter": "ه",
      "date": "2023-08-21T22:20:01.000000Z",
      "moshaf": [
        {
          "id": 317,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/H-Lharraz/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 306,
      "name": "عبدالله المشعل",
      "letter": "ع",
      "date": "2023-10-16T23:41:55.000000Z",
      "moshaf": [
        {
          "id": 318,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a-almishal/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 11,
          "moshaf_type": 11,
          "surah_list": "7,14,41,49,50,51,52,53,54,55,56"
        }
      ]
    },
    {
      "id": 307,
      "name": "عبدالعزيز سحيم",
      "letter": "ع",
      "date": "2023-11-06T00:22:23.000000Z",
      "moshaf": [
        {
          "id": 319,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server16.mp3quran.net/a_sheim/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 9,
          "moshaf_type": 21,
          "surah_list": "1,18,31,50,56,67,72,75,112"
        }
      ]
    },
    {
      "id": 31,
      "name": "سعود الشريم",
      "letter": "س",
      "date": "2020-04-07T02:17:33.000000Z",
      "moshaf": [
        {
          "id": 31,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server7.mp3quran.net/shur/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 32,
      "name": "سهل ياسين",
      "letter": "س",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 32,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/shl/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 33,
      "name": "زكي داغستاني",
      "letter": "ز",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 33,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/zaki/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 34,
      "name": "سامي الحسن",
      "letter": "س",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 34,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/sami_hsn/",
          "surah_total": 27,
          "moshaf_type": 11,
          "surah_list": "1,19,20,24,26,27,32,34,55,81,82,86,87,88,91,92,93,94,95,97,102,104,105,109,110,111,112"
        }
      ]
    },
    {
      "id": 35,
      "name": "سامي الدوسري",
      "letter": "س",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 35,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/sami_dosr/",
          "surah_total": 41,
          "moshaf_type": 11,
          "surah_list": "29,30,31,32,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 36,
      "name": "سيد رمضان",
      "letter": "س",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 36,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/sayed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 37,
      "name": "شعبان الصياد",
      "letter": "ش",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 37,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/shaban/",
          "surah_total": 20,
          "moshaf_type": 11,
          "surah_list": "3,35,87,88,89,90,91,92,94,95,96,97,98,99,100,101,102,103,104,105"
        }
      ]
    },
    {
      "id": 38,
      "name": "شيرزاد عبدالرحمن طاهر",
      "letter": "ش",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 38,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/taher/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 39,
      "name": "صابر عبدالحكم",
      "letter": "ص",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 39,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/hkm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 4,
      "name": "شيخ أبو بكر الشاطري",
      "letter": "ش",
      "date": "2020-05-04T23:34:13.000000Z",
      "moshaf": [
        {
          "id": 4,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/shatri/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 40,
      "name": "صالح الصاهود",
      "letter": "ص",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 40,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/sahood/",
          "surah_total": 110,
          "moshaf_type": 11,
          "surah_list": "1,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 41,
      "name": "صالح آل طالب",
      "letter": "ص",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 41,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/tlb/",
          "surah_total": 32,
          "moshaf_type": 11,
          "surah_list": "1,25,34,38,39,44,45,46,47,55,56,57,58,59,60,61,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86"
        }
      ]
    },
    {
      "id": 42,
      "name": "صالح الهبدان",
      "letter": "ص",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 42,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/habdan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 43,
      "name": "صلاح البدير",
      "letter": "ص",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 43,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/s_bud/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 44,
      "name": "صلاح الهاشم",
      "letter": "ص",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 45,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server12.mp3quran.net/salah_hashim_m/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 7,
          "moshaf_type": 51,
          "surah_list": "1,12,40,50,53,75,76"
        },
        {
          "id": 44,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/salah_hashim_m/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 46,
      "name": "صلاح بو خاطر",
      "letter": "ص",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 46,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/bu_khtr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 47,
      "name": "مختار الحاج",
      "letter": "م",
      "date": "2021-11-19T18:59:08.000000Z",
      "moshaf": [
        {
          "id": 283,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/mukhtar_haj/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 16,
          "moshaf_type": 11,
          "surah_list": "1,2,8,12,14,16,18,35,36,41,42,47,55,56,67,68"
        }
      ]
    },
    {
      "id": 48,
      "name": "عادل ريان",
      "letter": "ع",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 48,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/ryan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 49,
      "name": "عبدالبارئ الثبيتي",
      "letter": "ع",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 49,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/thubti/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 5,
      "name": "أحمد بن علي العجمي",
      "letter": "أ",
      "date": "2020-04-07T02:17:27.000000Z",
      "moshaf": [
        {
          "id": 5,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server10.mp3quran.net/ajm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 50,
      "name": "عبدالبارئ محمد",
      "letter": "ع",
      "date": "2020-04-07T02:17:38.000000Z",
      "moshaf": [
        {
          "id": 169,
          "name": "المصحف المعلم - المصحف المعلم",
          "server": "https://server12.mp3quran.net/bari/Almusshaf-Al-Mo-lim/",
          "surah_total": 91,
          "moshaf_type": 213,
          "surah_list": "1,3,5,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 50,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/bari/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 51,
      "name": "عبدالباسط عبدالصمد",
      "letter": "ع",
      "date": "2020-06-15T22:50:49.000000Z",
      "moshaf": [
        {
          "id": 53,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server7.mp3quran.net/basit/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 52,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server7.mp3quran.net/basit/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 51,
          "name": "المصحف المجود - المصحف المجود",
          "server": "https://server7.mp3quran.net/basit/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 54,
      "name": "عبدالرحمن السديس",
      "letter": "ع",
      "date": "2020-04-07T02:17:38.000000Z",
      "moshaf": [
        {
          "id": 54,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/sds/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 55,
      "name": "عبدالعزيز الأحمد",
      "letter": "ع",
      "date": "2020-04-07T02:17:38.000000Z",
      "moshaf": [
        {
          "id": 55,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/a_ahmed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 56,
      "name": "عبدالعزيز الزهراني",
      "letter": "ع",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 56,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/zahrani/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 57,
      "name": "عبدالله البريمي",
      "letter": "ع",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 57,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/brmi/",
          "surah_total": 41,
          "moshaf_type": 11,
          "surah_list": "1,49,50,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95"
        }
      ]
    },
    {
      "id": 58,
      "name": "عبدالله البعيجان",
      "letter": "ع",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 58,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/buajan/",
          "surah_total": 83,
          "moshaf_type": 11,
          "surah_list": "1,8,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,28,29,30,32,33,34,35,39,40,41,42,43,48,49,50,55,56,57,60,62,63,64,65,66,67,68,69,73,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 59,
      "name": "عبدالله المطرود",
      "letter": "ع",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 59,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/mtrod/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 6,
      "name": "أحمد الحواشي",
      "letter": "أ",
      "date": "2020-04-07T02:17:27.000000Z",
      "moshaf": [
        {
          "id": 6,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/hawashi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 60,
      "name": "عبدالله بصفر",
      "letter": "ع",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 60,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/bsfr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 61,
      "name": "عبدالله خياط",
      "letter": "ع",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 61,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/kyat/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 62,
      "name": "عبدالله عواد الجهني",
      "letter": "ع",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 62,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server13.mp3quran.net/jhn/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 63,
      "name": "عبدالله غيلان",
      "letter": "ع",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 63,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/gulan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 64,
      "name": "عبدالرشيد صوفي",
      "letter": "ع",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 258,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/soufi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 65,
          "name": "السوسي عن أبي عمرو - مرتل",
          "server": "https://server16.mp3quran.net/soufi/Rewayat-Assosi-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 71,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 64,
          "name": "خلف عن حمزة - مرتل",
          "server": "https://server16.mp3quran.net/soufi/Rewayat-Khalaf-A-n-Hamzah/",
          "surah_total": 114,
          "moshaf_type": 31,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 66,
      "name": "عبدالمحسن الحارثي",
      "letter": "ع",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 66,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/mohsin_harthi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 67,
      "name": "عبدالمحسن القاسم",
      "letter": "ع",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 67,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/qasm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 68,
      "name": "عبدالمحسن العسكر",
      "letter": "ع",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 68,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/askr/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,2,7,55"
        }
      ]
    },
    {
      "id": 69,
      "name": "عبدالمحسن العبيكان",
      "letter": "ع",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 69,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/obk/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 7,
      "name": "أحمد سعود",
      "letter": "أ",
      "date": "2020-04-07T02:17:27.000000Z",
      "moshaf": [
        {
          "id": 7,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/saud/",
          "surah_total": 30,
          "moshaf_type": 11,
          "surah_list": "85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 70,
      "name": "عبدالهادي أحمد كناكري",
      "letter": "ع",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 70,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/kanakeri/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 71,
      "name": "عبدالودود حنيف",
      "letter": "ع",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 71,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/wdod/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 72,
      "name": "عبدالولي الأركاني",
      "letter": "ع",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 72,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/arkani/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 73,
      "name": "علي أبو هاشم",
      "letter": "ع",
      "date": "2020-04-07T02:17:43.000000Z",
      "moshaf": [
        {
          "id": 73,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/abo_hashim/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "50,51,52,53,54,55,56,57"
        }
      ]
    },
    {
      "id": 74,
      "name": "علي بن عبدالرحمن الحذيفي",
      "letter": "ع",
      "date": "2020-06-17T14:45:14.000000Z",
      "moshaf": [
        {
          "id": 305,
          "name": "شعبة  عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/hthfi/Rewayat-Sho-bah-A-n-Asim/",
          "surah_total": 114,
          "moshaf_type": 151,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 75,
          "name": "قالون عن نافع - مرتل",
          "server": "https://server9.mp3quran.net/huthifi_qalon/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 74,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/hthfi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 76,
      "name": "علي جابر",
      "letter": "ع",
      "date": "2020-04-07T02:17:43.000000Z",
      "moshaf": [
        {
          "id": 76,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/a_jbr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 77,
      "name": "علي حجاج السويسي",
      "letter": "ع",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 77,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/hajjaj/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 78,
      "name": "عماد زهير حافظ",
      "letter": "ع",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 78,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/hafz/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 79,
      "name": "عبدالعزيز التركي",
      "letter": "ع",
      "date": "2021-11-16T16:30:45.000000Z",
      "moshaf": [
        {
          "id": 282,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_turki/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 66,
          "moshaf_type": 11,
          "surah_list": "1,2,6,7,8,9,10,11,12,13,18,21,24,25,26,27,28,29,30,31,39,40,41,44,46,48,49,54,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 8,
      "name": "أحمد صابر",
      "letter": "أ",
      "date": "2020-04-07T02:17:28.000000Z",
      "moshaf": [
        {
          "id": 8,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/saber/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 80,
      "name": "عمر القزابري",
      "letter": "ع",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 80,
          "name": "ورش عن نافع - مرتل",
          "server": "https://server9.mp3quran.net/omar_warsh/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 81,
      "name": "فارس عباد",
      "letter": "ف",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 81,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/frs_a/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 82,
      "name": "فهد العتيبي",
      "letter": "ف",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 82,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/fahad_otibi/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "50,56,69,72,73,74,75,76"
        }
      ]
    },
    {
      "id": 83,
      "name": "فهد الكندري",
      "letter": "ف",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 83,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/kndri/",
          "surah_total": 53,
          "moshaf_type": 11,
          "surah_list": "12,36,51,52,53,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 84,
      "name": "فواز الكعبي",
      "letter": "ف",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 84,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/fawaz/",
          "surah_total": 44,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,25,27,28,29,30,36,39,40,49,54,55,56,57,58,59,62,63,66,67,73,87,109,112"
        }
      ]
    },
    {
      "id": 85,
      "name": "لافي العوني",
      "letter": "ل",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 85,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/lafi/",
          "surah_total": 52,
          "moshaf_type": 11,
          "surah_list": "3,12,15,16,19,20,27,28,30,31,32,33,36,37,38,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 86,
      "name": "ناصر القطامي",
      "letter": "ن",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 86,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/qtm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 87,
      "name": "نبيل الرفاعي",
      "letter": "ن",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 87,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/nabil/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 88,
      "name": "نعمة الحسان",
      "letter": "ن",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 88,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/namh/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 89,
      "name": "هاني الرفاعي",
      "letter": "ه",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 89,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/hani/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 9,
      "name": "أحمد نعينع",
      "letter": "أ",
      "date": "2020-04-07T02:17:28.000000Z",
      "moshaf": [
        {
          "id": 9,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/ahmad_nu/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 90,
      "name": "وليد الدليمي",
      "letter": "و",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 90,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server8.mp3quran.net/dlami/",
          "surah_total": 51,
          "moshaf_type": 11,
          "surah_list": "1,12,17,31,39,41,45,48,49,50,51,52,53,54,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 91,
      "name": "وليد النائحي",
      "letter": "و",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 91,
          "name": "قالون عن نافع من طريق أبي نشيط - مرتل",
          "server": "https://server9.mp3quran.net/waleed/",
          "surah_total": 114,
          "moshaf_type": 81,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 92,
      "name": "ياسر الدوسري",
      "letter": "ي",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 92,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server11.mp3quran.net/yasser/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 93,
      "name": "ياسر القرشي",
      "letter": "ي",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 93,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/qurashi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 94,
      "name": "ياسر الفيلكاوي",
      "letter": "ي",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 94,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server6.mp3quran.net/fyl/",
          "surah_total": 52,
          "moshaf_type": 11,
          "surah_list": "1,2,25,44,56,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,114"
        }
      ]
    },
    {
      "id": 95,
      "name": "ياسر المزروعي ",
      "letter": "ي",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 95,
          "name": "قراءة يعقوب الحضرمي بروايتي رويس وروح - مرتل",
          "server": "https://server9.mp3quran.net/mzroyee/",
          "surah_total": 114,
          "moshaf_type": 91,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 96,
      "name": "يحيى حوا",
      "letter": "ي",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 96,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server12.mp3quran.net/yahya/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 97,
      "name": "يوسف الشويعي",
      "letter": "ي",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 97,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server9.mp3quran.net/yousef/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 98,
      "name": "عبدالله عبدل",
      "letter": "ع",
      "date": "2021-11-22T19:47:40.000000Z",
      "moshaf": [
        {
          "id": 284,
          "name": "حفص عن عاصم - مرتل",
          "server": "https://server16.mp3quran.net/a_abdl/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    }
  ]
en_reciters =  [
    {
      "id": 1,
      "name": "Ibrahim Al-Akdar",
      "letter": "I",
      "date": "2020-04-07T02:17:26.000000Z",
      "moshaf": [
        {
          "id": 1,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/akdr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 10,
      "name": "Akram Alalaqmi",
      "letter": "A",
      "date": "2020-04-07T02:17:28.000000Z",
      "moshaf": [
        {
          "id": 10,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/akrm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 100,
      "name": "Majed Al-Enezi",
      "letter": "M",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 100,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/majd_onazi/",
          "surah_total": 69,
          "moshaf_type": 11,
          "surah_list": "1,13,14,17,18,19,30,31,32,34,43,44,45,49,50,51,53,55,56,59,60,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 101,
      "name": "Malik shaibat Alhamed",
      "letter": "M",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 101,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/shaibat/",
          "surah_total": 37,
          "moshaf_type": 11,
          "surah_list": "78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 102,
      "name": "Maher Al Meaqli",
      "letter": "M",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 133,
          "name": "Almusshaf Al Mojawwad - Almusshaf Al Mojawwad",
          "server": "https://server12.mp3quran.net/maher/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 103,
          "name": "Almusshaf Al Mo'lim - Almusshaf Al Mo'lim",
          "server": "https://server12.mp3quran.net/maher/Almusshaf-Al-Mo-lim/",
          "surah_total": 38,
          "moshaf_type": 213,
          "surah_list": "1,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 102,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/maher/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 104,
      "name": "Mohammad Al-Airawy",
      "letter": "M",
      "date": "2020-04-07T02:17:49.000000Z",
      "moshaf": [
        {
          "id": 104,
          "name": "Rewayat Warsh A'n Nafi' Men Tariq Alazraq - Murattal",
          "server": "https://server6.mp3quran.net/earawi/",
          "surah_total": 112,
          "moshaf_type": 181,
          "surah_list": "1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 105,
      "name": "Mohammed Al-Barrak",
      "letter": "M",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 105,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server13.mp3quran.net/braak/",
          "surah_total": 62,
          "moshaf_type": 11,
          "surah_list": "1,12,36,37,44,45,50,51,52,53,54,55,56,57,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 106,
      "name": "Mohammad Al-Tablaway",
      "letter": "M",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 106,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/tblawi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 107,
      "name": "Mohammed Al-Lohaidan",
      "letter": "M",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 107,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/lhdan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 108,
      "name": "Mohammed Al-Muhasny",
      "letter": "M",
      "date": "2020-04-07T02:17:50.000000Z",
      "moshaf": [
        {
          "id": 108,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/mhsny/",
          "surah_total": 113,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 109,
      "name": "Mohammed Ayyub",
      "letter": "M",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 320,
          "name": "Rewayat Hafs A'n Assem - 4",
          "server": "https://server16.mp3quran.net/ayyoub2/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 14,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 109,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/ayyub/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 11,
      "name": "Alhusayni Al-Azazi",
      "letter": "A",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 11,
          "name": "Almusshaf Al Mo'lim - Almusshaf Al Mo'lim",
          "server": "https://server8.mp3quran.net/3zazi/",
          "surah_total": 57,
          "moshaf_type": 213,
          "surah_list": "58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 110,
      "name": "Mohammad Saleh Alim Shah",
      "letter": "M",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 110,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/shah/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 111,
      "name": "Mohammed Jibreel",
      "letter": "M",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 111,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/jbrl/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 112,
      "name": "Mohammed Siddiq Al-Minshawi",
      "letter": "M",
      "date": "2020-04-07T02:17:51.000000Z",
      "moshaf": [
        {
          "id": 114,
          "name": "Almusshaf Al Mo'lim - Almusshaf Al Mo'lim",
          "server": "https://server10.mp3quran.net/minsh/Almusshaf-Al-Mo-lim/",
          "surah_total": 114,
          "moshaf_type": 213,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 113,
          "name": "Almusshaf Al Mojawwad - Almusshaf Al Mojawwad",
          "server": "https://server10.mp3quran.net/minsh/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 112,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/minsh/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 115,
      "name": "Mohammad Abdullkarem",
      "letter": "M",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 210,
          "name": "Rewayat Warsh A'n Nafi' Men  Tariq Abi Baker Alasbahani - Murattal",
          "server": "https://server12.mp3quran.net/m_krm/Rewayat-Warsh-A-n-Nafi-Men-Tariq-Abi-Baker-Alasbahani/",
          "surah_total": 114,
          "moshaf_type": 101,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 115,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/m_krm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 116,
      "name": "Mohammad Al-Abdullah",
      "letter": "M",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 117,
          "name": "Rewayat AlDorai A'n Al-Kisa'ai - Murattal",
          "server": "https://server9.mp3quran.net/abdullah/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 114,
          "moshaf_type": 121,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 116,
          "name": "Rewayat Albizi and Qunbol A'n Ibn Katheer - Murattal",
          "server": "https://server9.mp3quran.net/abdullah/",
          "surah_total": 114,
          "moshaf_type": 111,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 118,
      "name": "Mahmoud Khalil Al-Hussary",
      "letter": "M",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 270,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server13.mp3quran.net/husr/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 269,
          "name": "Rewayat Aldori A'n Abi Amr - Murattal",
          "server": "https://server13.mp3quran.net/husr/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 120,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server13.mp3quran.net/husr/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 119,
          "name": "Almusshaf Al Mojawwad - Almusshaf Al Mojawwad",
          "server": "https://server13.mp3quran.net/husr/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 118,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server13.mp3quran.net/husr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 12,
      "name": "Idrees Abkr",
      "letter": "I",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 12,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/abkr/",
          "surah_total": 111,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,47,48,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 121,
      "name": "Mahmoud Ali  Albanna",
      "letter": "M",
      "date": "2020-04-07T02:17:52.000000Z",
      "moshaf": [
        {
          "id": 122,
          "name": "Almusshaf Al Mojawwad - Almusshaf Al Mojawwad",
          "server": "https://server8.mp3quran.net/bna/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 121,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/bna/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 123,
      "name": "Mishary Alafasi",
      "letter": "M",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 124,
          "name": "Rewayat AlDorai A'n Al-Kisa'ai - Murattal",
          "server": "https://server8.mp3quran.net/afs/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 5,
          "moshaf_type": 121,
          "surah_list": "14,25,87,97,99"
        },
        {
          "id": 123,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/afs/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 125,
      "name": "Mustafa Ismail",
      "letter": "M",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 288,
          "name": "Almusshaf Al Mojawwad - Almusshaf Al Mojawwad",
          "server": "https://server8.mp3quran.net/mustafa/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 125,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/mustafa/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 126,
      "name": "Mustafa Al-Lahoni",
      "letter": "M",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 126,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/lahoni/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 127,
      "name": "Mustafa raad Alazawy",
      "letter": "M",
      "date": "2020-04-07T02:17:53.000000Z",
      "moshaf": [
        {
          "id": 127,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/ra3ad/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 128,
      "name": "Muamar (From Indonesia)",
      "letter": "M",
      "date": "2020-04-07T02:17:54.000000Z",
      "moshaf": [
        {
          "id": 128,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/muamr/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "36,93,94,97,101,109,110,111"
        }
      ]
    },
    {
      "id": 129,
      "name": "Muftah Alsaltany",
      "letter": "M",
      "date": "2024-04-22T22:29:17.000000Z",
      "moshaf": [
        {
          "id": 196,
          "name": "Ibn Thakwan A'n Ibn Amer - Murattal",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat_Ibn-Thakwan-A-n-Ibn-Amer/",
          "surah_total": 114,
          "moshaf_type": 161,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 195,
          "name": "Sho'bah A'n Asim - Murattal",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat_Sho-bah-A-n-Asim/",
          "surah_total": 77,
          "moshaf_type": 151,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77"
        },
        {
          "id": 182,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 180,
          "name": "Rewayat AlDorai A'n Al-Kisa'ai - Murattal",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 114,
          "moshaf_type": 121,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 129,
          "name": "Rewayat Aldori A'n Abi Amr - Murattal",
          "server": "https://server14.mp3quran.net/muftah_sultany/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 13,
      "name": "Alzain Mohammad Ahmad",
      "letter": "A",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 13,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/alzain/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 134,
      "name": "Mohammad Saayed",
      "letter": "M",
      "date": "2021-05-06T11:13:52.000000Z",
      "moshaf": [
        {
          "id": 134,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/m_sayed/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 135,
      "name": "Abdulrahman Alsuwayid",
      "letter": "A",
      "date": "2021-05-19T14:25:00.000000Z",
      "moshaf": [
        {
          "id": 135,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_swaiyd/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 85,
          "moshaf_type": 11,
          "surah_list": "2,11,15,18,19,25,34,35,36,37,38,39,40,41,42,43,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 136,
      "name": "Abdulelah bin Aoun",
      "letter": "A",
      "date": "2021-05-20T13:46:47.000000Z",
      "moshaf": [
        {
          "id": 136,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_binaoun/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 137,
      "name": "Ahmad Talib bin Humaid",
      "letter": "A",
      "date": "2021-05-29T16:44:43.000000Z",
      "moshaf": [
        {
          "id": 137,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_binhameed/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 82,
          "moshaf_type": 11,
          "surah_list": "1,2,5,6,8,10,12,18,20,29,30,31,32,35,37,38,44,45,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 138,
      "name": "Noreen Mohammad Siddiq",
      "letter": "N",
      "date": "2021-06-29T11:08:49.000000Z",
      "moshaf": [
        {
          "id": 138,
          "name": "Rewayat Aldori A'n Abi Amr - Murattal",
          "server": "https://server16.mp3quran.net/nourin_siddig/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 139,
      "name": "Majed Al-Zamil",
      "letter": "M",
      "date": "2020-04-07T02:17:54.000000Z",
      "moshaf": [
        {
          "id": 139,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/zaml/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 14,
      "name": "Al-Qaria Yassen",
      "letter": "A",
      "date": "2020-04-07T02:17:29.000000Z",
      "moshaf": [
        {
          "id": 14,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server11.mp3quran.net/qari/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 149,
      "name": "Maher Shakhashero",
      "letter": "M",
      "date": "2020-04-07T02:17:54.000000Z",
      "moshaf": [
        {
          "id": 149,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/shaksh/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 15,
      "name": "Alashri Omran",
      "letter": "A",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 15,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/omran/",
          "surah_total": 113,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 150,
      "name": "Mohammad AlMonshed",
      "letter": "M",
      "date": "2020-04-07T02:17:55.000000Z",
      "moshaf": [
        {
          "id": 150,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/monshed/",
          "surah_total": 110,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,83,84,85,86,87,88,90,91,92,93,94,95,96,97,98,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 151,
      "name": "Mahmood AlSheimy",
      "letter": "M",
      "date": "2020-04-07T02:17:55.000000Z",
      "moshaf": [
        {
          "id": 151,
          "name": "Rewayat AlDorai A'n Al-Kisa'ai - Murattal",
          "server": "https://server10.mp3quran.net/sheimy/",
          "surah_total": 114,
          "moshaf_type": 121,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 152,
      "name": "Yasser Salamah",
      "letter": "Y",
      "date": "2020-04-07T02:17:55.000000Z",
      "moshaf": [
        {
          "id": 152,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/salamah/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 153,
      "name": "Akhil Abdulhayy Rawa",
      "letter": "A",
      "date": "2022-06-23T10:49:15.000000Z",
      "moshaf": [
        {
          "id": 153,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/akil/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "50,51,52,56"
        }
      ]
    },
    {
      "id": 154,
      "name": "Ustaz Zamri",
      "letter": "U",
      "date": "2022-06-23T10:49:03.000000Z",
      "moshaf": [
        {
          "id": 154,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/zamri/",
          "surah_total": 7,
          "moshaf_type": 11,
          "surah_list": "32,44,55,56,61,67,76"
        }
      ]
    },
    {
      "id": 159,
      "name": "Khalid Almohana",
      "letter": "K",
      "date": "2020-04-07T02:17:56.000000Z",
      "moshaf": [
        {
          "id": 159,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/mohna/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 16,
      "name": "Aloyoon Al-Koshi",
      "letter": "A",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 16,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server11.mp3quran.net/koshi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 160,
      "name": "Adel Al-Khalbany",
      "letter": "A",
      "date": "2020-04-07T02:17:56.000000Z",
      "moshaf": [
        {
          "id": 160,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/a_klb/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 161,
      "name": "Mousa Bilal",
      "letter": "M",
      "date": "2020-04-07T02:17:56.000000Z",
      "moshaf": [
        {
          "id": 161,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/bilal/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 162,
      "name": "Hussain Alshaik",
      "letter": "H",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 162,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/alshaik/",
          "surah_total": 15,
          "moshaf_type": 11,
          "surah_list": "13,14,22,32,38,44,45,49,50,78,79,80,81,82,85"
        }
      ]
    },
    {
      "id": 163,
      "name": "Hatem Fareed Alwaer",
      "letter": "H",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 163,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/hatem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 164,
      "name": "Ibrahim Aljormy",
      "letter": "I",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 164,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/jormy/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 165,
      "name": "Mahmood Al rifai",
      "letter": "M",
      "date": "2020-04-07T02:17:57.000000Z",
      "moshaf": [
        {
          "id": 165,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/mrifai/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 166,
      "name": "Nasser Al obaid",
      "letter": "N",
      "date": "2020-04-07T02:17:58.000000Z",
      "moshaf": [
        {
          "id": 166,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/obaid/",
          "surah_total": 9,
          "moshaf_type": 11,
          "surah_list": "7,13,14,15,25,26,27,40,41"
        }
      ]
    },
    {
      "id": 167,
      "name": "Wasel Almethen",
      "letter": "W",
      "date": "2020-04-07T02:17:58.000000Z",
      "moshaf": [
        {
          "id": 167,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/wasel/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 9,
          "moshaf_type": 11,
          "surah_list": "8,9,36,38,42,45,50,59,60"
        }
      ]
    },
    {
      "id": 17,
      "name": "Tawfeeq As-Sayegh",
      "letter": "T",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 17,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/twfeeq/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 178,
      "name": "Ibrahim Aldosari",
      "letter": "I",
      "date": "2022-06-23T10:51:41.000000Z",
      "moshaf": [
        {
          "id": 232,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/ibrahim_dosri/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 178,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server10.mp3quran.net/ibrahim_dosri/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 18,
      "name": "Jamal Shaker Abdullah",
      "letter": "J",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 18,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/jamal/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 181,
      "name": "Jamaan Alosaimi",
      "letter": "J",
      "date": "2020-04-07T02:17:58.000000Z",
      "moshaf": [
        {
          "id": 181,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/jaman/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 183,
      "name": "Rodziah Abdulrahman",
      "letter": "R",
      "date": "2022-06-23T10:48:49.000000Z",
      "moshaf": [
        {
          "id": 183,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/rziah/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "3,8,33,35"
        }
      ]
    },
    {
      "id": 184,
      "name": "Rogayah Sulong",
      "letter": "R",
      "date": "2022-06-23T10:48:41.000000Z",
      "moshaf": [
        {
          "id": 184,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/rogiah/",
          "surah_total": 1,
          "moshaf_type": 11,
          "surah_list": "36"
        }
      ]
    },
    {
      "id": 185,
      "name": "Sapinah Mamat",
      "letter": "S",
      "date": "2022-06-23T10:48:31.000000Z",
      "moshaf": [
        {
          "id": 185,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/mamat/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "3,14,21,22"
        }
      ]
    },
    {
      "id": 187,
      "name": "Saidin Abdulrahman",
      "letter": "S",
      "date": "2022-06-23T10:48:22.000000Z",
      "moshaf": [
        {
          "id": 187,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/sideen/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "17,23,56,75"
        }
      ]
    },
    {
      "id": 188,
      "name": "Abdulghani Abdullah",
      "letter": "A",
      "date": "2022-06-23T10:48:12.000000Z",
      "moshaf": [
        {
          "id": 188,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/abdulgani/",
          "surah_total": 13,
          "moshaf_type": 11,
          "surah_list": "1,2,5,6,9,67,87,91,92,94,95,97,114"
        }
      ]
    },
    {
      "id": 189,
      "name": "Abdullah Fahmi",
      "letter": "A",
      "date": "2022-06-23T10:48:03.000000Z",
      "moshaf": [
        {
          "id": 189,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/fhmi/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,36,53,75"
        }
      ]
    },
    {
      "id": 19,
      "name": "Hamad Al Daghriri",
      "letter": "H",
      "date": "2020-04-07T02:17:30.000000Z",
      "moshaf": [
        {
          "id": 19,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/hamad/",
          "surah_total": 5,
          "moshaf_type": 11,
          "surah_list": "1,12,13,43,44"
        }
      ]
    },
    {
      "id": 190,
      "name": "Muhammad Al-Hafiz",
      "letter": "M",
      "date": "2022-06-23T10:47:45.000000Z",
      "moshaf": [
        {
          "id": 190,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/hafz/",
          "surah_total": 3,
          "moshaf_type": 11,
          "surah_list": "1,19,31"
        }
      ]
    },
    {
      "id": 191,
      "name": "Mohammed Hafas Ali",
      "letter": "M",
      "date": "2022-06-23T10:47:14.000000Z",
      "moshaf": [
        {
          "id": 191,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/hfs/",
          "surah_total": 5,
          "moshaf_type": 11,
          "surah_list": "1,9,11,13,67"
        }
      ]
    },
    {
      "id": 192,
      "name": "Muhammed Khairul Anuar",
      "letter": "M",
      "date": "2020-10-19T15:36:39.000000Z",
      "moshaf": [
        {
          "id": 192,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/malaysia/nor/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,12,19,31"
        }
      ]
    },
    {
      "id": 193,
      "name": "Yousef Bin Noah Ahmad",
      "letter": "Y",
      "date": "2020-04-07T02:18:01.000000Z",
      "moshaf": [
        {
          "id": 193,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/noah/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 194,
      "name": "Jamal Addeen Alzailaie",
      "letter": "J",
      "date": "2020-04-07T02:18:01.000000Z",
      "moshaf": [
        {
          "id": 194,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/zilaie/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "1,19,32,54,67,70,73,91"
        }
      ]
    },
    {
      "id": 197,
      "name": "Moeedh Alharthi",
      "letter": "M",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 197,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/harthi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 198,
      "name": "Mohammad Rashad Alshareef",
      "letter": "M",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 198,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/rashad/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 2,
      "name": "Ibrahim Al-Jebreen",
      "letter": "I",
      "date": "2020-04-07T02:17:26.000000Z",
      "moshaf": [
        {
          "id": 2,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/jbreen/",
          "surah_total": 99,
          "moshaf_type": 11,
          "surah_list": "1,3,4,7,8,10,12,13,14,15,16,17,18,19,20,21,23,25,27,31,32,33,34,36,37,38,39,40,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 20,
      "name": "Khalid Al-Jileel",
      "letter": "K",
      "date": "2020-04-07T02:17:31.000000Z",
      "moshaf": [
        {
          "id": 20,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/jleel/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 201,
      "name": "Ahmed Al-trabulsi",
      "letter": "A",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 201,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/trabulsi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 199,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server10.mp3quran.net/trablsi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 202,
      "name": "Abdullah Al-Kandari",
      "letter": "A",
      "date": "2020-04-07T02:18:02.000000Z",
      "moshaf": [
        {
          "id": 202,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/Abdullahk/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 203,
      "name": "Ahmed Amer",
      "letter": "A",
      "date": "2020-04-07T02:18:03.000000Z",
      "moshaf": [
        {
          "id": 203,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/Aamer/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 204,
      "name": "Ibrahem Assadan",
      "letter": "I",
      "date": "2022-06-23T10:50:29.000000Z",
      "moshaf": [
        {
          "id": 204,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/IbrahemSadan/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,6,19,20"
        }
      ]
    },
    {
      "id": 205,
      "name": "Ahmad Alhuthaifi",
      "letter": "A",
      "date": "2020-04-07T02:18:03.000000Z",
      "moshaf": [
        {
          "id": 205,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/ahmad_huth/",
          "surah_total": 105,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,35,38,41,42,43,44,45,47,48,49,50,51,52,53,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 206,
      "name": "Mohammed Osman Khan",
      "letter": "M",
      "date": "2020-06-15T22:08:39.000000Z",
      "moshaf": [
        {
          "id": 206,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/khan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 207,
      "name": "Youssef Edghouch",
      "letter": "Y",
      "date": "2020-06-15T21:51:49.000000Z",
      "moshaf": [
        {
          "id": 207,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server7.mp3quran.net/dgsh/",
          "surah_total": 22,
          "moshaf_type": 11,
          "surah_list": "1,3,55,67,71,75,82,85,90,91,92,100,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 208,
      "name": "Addokali Mohammad Alalim",
      "letter": "A",
      "date": "2020-04-07T02:18:04.000000Z",
      "moshaf": [
        {
          "id": 208,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server7.mp3quran.net/dokali/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 209,
      "name": "Wishear Hayder Arbili",
      "letter": "W",
      "date": "2020-04-07T02:18:04.000000Z",
      "moshaf": [
        {
          "id": 209,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/wishear/",
          "surah_total": 2,
          "moshaf_type": 11,
          "surah_list": "55,56"
        }
      ]
    },
    {
      "id": 21,
      "name": "Khaled Al-Qahtani",
      "letter": "K",
      "date": "2020-04-07T02:17:31.000000Z",
      "moshaf": [
        {
          "id": 21,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/qht/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 211,
      "name": "Alfateh Alzubair",
      "letter": "A",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 211,
          "name": "Rewayat Aldori A'n Abi Amr - Murattal",
          "server": "https://server6.mp3quran.net/fateh/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21181,
      "name": "Muhammad Burhaji",
      "letter": "M",
      "date": "2024-03-20T22:13:58.000000Z",
      "moshaf": [
        {
          "id": 340,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/M_Burhaji/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21182,
      "name": "Yusuf ALaidroos",
      "letter": "Y",
      "date": "2024-09-04T01:26:29.000000Z",
      "moshaf": [
        {
          "id": 10904,
          "name": "Rewayat Hafs A'n Assem - 4",
          "server": "https://server16.mp3quran.net/Y_ALaidroos/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 99,
          "moshaf_type": 14,
          "surah_list": "1,2,3,4,5,7,8,9,10,11,12,14,15,17,18,19,24,26,27,28,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21183,
      "name": "Hassan Aldaghriri",
      "letter": "H",
      "date": "2024-12-04T16:33:47.000000Z",
      "moshaf": [
        {
          "id": 10905,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/H-Aldaghriri/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21184,
      "name": "Muhammad Al Faqih",
      "letter": "M",
      "date": "2024-12-18T20:27:10.000000Z",
      "moshaf": [
        {
          "id": 10906,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/M_Alfaqih/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21185,
      "name": "Ahmed Albishr",
      "letter": "A",
      "date": "2024-12-25T13:47:02.000000Z",
      "moshaf": [
        {
          "id": 10907,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_albishr/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 21186,
      "name": "Junaid Adam Abdullah",
      "letter": "J",
      "date": "2025-02-09T20:21:02.000000Z",
      "moshaf": [
        {
          "id": 10908,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/J-Abdullah/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 212,
      "name": "Tareq Abdulgani daawob",
      "letter": "T",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 212,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server10.mp3quran.net/tareq/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 216,
      "name": "Othman Al-Ansary",
      "letter": "O",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 216,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/Othmn/",
          "surah_total": 76,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 217,
      "name": "Bandar Balilah",
      "letter": "B",
      "date": "2020-04-07T02:18:05.000000Z",
      "moshaf": [
        {
          "id": 217,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/balilah/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 218,
      "name": "Khalid Al-Shoraimy",
      "letter": "K",
      "date": "2020-04-07T02:18:06.000000Z",
      "moshaf": [
        {
          "id": 218,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/shoraimy/",
          "surah_total": 73,
          "moshaf_type": 11,
          "surah_list": "1,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 219,
      "name": "Wadeea Al-Yamani",
      "letter": "W",
      "date": "2020-04-07T02:18:06.000000Z",
      "moshaf": [
        {
          "id": 219,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/wdee3/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 22,
      "name": "Khalid Abdulkafi",
      "letter": "K",
      "date": "2020-04-07T02:17:31.000000Z",
      "moshaf": [
        {
          "id": 22,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/kafi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 221,
      "name": "Raad Al Kurdi",
      "letter": "R",
      "date": "2020-04-07T02:18:06.000000Z",
      "moshaf": [
        {
          "id": 221,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/kurdi/",
          "surah_total": 93,
          "moshaf_type": 11,
          "surah_list": "1,2,3,12,13,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,35,36,37,38,39,41,42,43,44,46,47,48,51,52,56,57,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 225,
      "name": "Abdulrahman Aloosi",
      "letter": "A",
      "date": "2023-10-04T21:50:14.000000Z",
      "moshaf": [
        {
          "id": 225,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/aloosi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 226,
      "name": "Khalid Algamdi",
      "letter": "K",
      "date": "2020-04-07T02:18:07.000000Z",
      "moshaf": [
        {
          "id": 226,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/ghamdi/",
          "surah_total": 28,
          "moshaf_type": 11,
          "surah_list": "1,6,9,14,21,25,30,42,50,52,53,54,58,59,60,61,65,67,68,69,70,71,77,85,86,88,91,93"
        }
      ]
    },
    {
      "id": 227,
      "name": "Ramadan Shakoor",
      "letter": "R",
      "date": "2020-04-07T02:18:07.000000Z",
      "moshaf": [
        {
          "id": 227,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/shakoor/",
          "surah_total": 61,
          "moshaf_type": 11,
          "surah_list": "1,3,10,13,14,23,26,29,35,36,39,40,42,43,47,48,49,50,51,57,58,59,60,63,68,69,70,71,72,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,111,112,113,114"
        }
      ]
    },
    {
      "id": 228,
      "name": "Abdulmajeed Al-Arkani",
      "letter": "A",
      "date": "2020-04-07T02:18:07.000000Z",
      "moshaf": [
        {
          "id": 228,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server7.mp3quran.net/m_arkani/",
          "surah_total": 46,
          "moshaf_type": 11,
          "surah_list": "12,18,19,21,22,40,50,56,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 229,
      "name": "Mohammad Khalil Al-Qari",
      "letter": "M",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 229,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/m_qari/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 23,
      "name": "Khalid Al-Wehabi",
      "letter": "K",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 23,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/whabi/",
          "surah_total": 11,
          "moshaf_type": 11,
          "surah_list": "12,13,14,16,19,24,25,29,30,31,32"
        }
      ]
    },
    {
      "id": 230,
      "name": "Rami Aldeais",
      "letter": "R",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 230,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/rami/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 231,
      "name": "Hazza Al-Balushi",
      "letter": "H",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 231,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/hazza/",
          "surah_total": 75,
          "moshaf_type": 11,
          "surah_list": "1,13,14,15,18,19,25,29,30,31,36,37,38,39,40,42,44,47,49,50,51,52,53,54,55,56,57,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 236,
      "name": "Abdulrahman Al-Majed",
      "letter": "A",
      "date": "2020-04-07T02:18:08.000000Z",
      "moshaf": [
        {
          "id": 236,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/a_majed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 237,
      "name": "Marwan Alakri",
      "letter": "M",
      "date": "2022-02-02T17:25:47.000000Z",
      "moshaf": [
        {
          "id": 287,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/m_akri/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 24,
      "name": "Khalifa Altunaiji",
      "letter": "K",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 24,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/tnjy/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 240,
      "name": "Salman Alotaibi",
      "letter": "S",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 240,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/salman/",
          "surah_total": 61,
          "moshaf_type": 11,
          "surah_list": "1,2,36,46,56,58,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 241,
      "name": "Mohammad Refat",
      "letter": "M",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 241,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/refat/",
          "surah_total": 31,
          "moshaf_type": 11,
          "surah_list": "1,10,11,12,17,18,19,20,48,54,55,56,69,72,73,75,76,77,78,79,81,82,83,85,86,87,88,89,96,98,100"
        }
      ]
    },
    {
      "id": 243,
      "name": "Abdullah Al-Mousa",
      "letter": "A",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 286,
          "name": "Almusshaf Al Mo'lim - Almusshaf Al Mo'lim",
          "server": "https://server14.mp3quran.net/mousa/Almusshaf-Al-Mo-lim/",
          "surah_total": 38,
          "moshaf_type": 213,
          "surah_list": "1,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 243,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/mousa/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 102,
          "moshaf_type": 11,
          "surah_list": "1,2,3,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,29,31,32,33,35,36,37,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 244,
      "name": "Abdullah Al-Khalaf",
      "letter": "A",
      "date": "2020-04-07T02:18:09.000000Z",
      "moshaf": [
        {
          "id": 244,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/khalf/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 245,
      "name": "Mansour Al-Salemi",
      "letter": "M",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 245,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/mansor/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 246,
      "name": "Salah Musali",
      "letter": "S",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 246,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/musali/",
          "surah_total": 48,
          "moshaf_type": 11,
          "surah_list": "67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 247,
      "name": "Khalid Alsharekh",
      "letter": "K",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 247,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/sharekh/",
          "surah_total": 64,
          "moshaf_type": 11,
          "surah_list": "2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 248,
      "name": "Nasser Alosfor",
      "letter": "N",
      "date": "2020-04-07T02:18:10.000000Z",
      "moshaf": [
        {
          "id": 248,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/alosfor/",
          "surah_total": 111,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 25,
      "name": "Dawood Hamza",
      "letter": "D",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 25,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/hamza/",
          "surah_total": 86,
          "moshaf_type": 11,
          "surah_list": "2,3,5,6,7,8,10,12,14,16,17,18,19,20,21,23,24,25,27,28,29,31,33,34,35,36,37,38,40,41,42,46,47,48,50,52,53,54,56,58,60,61,63,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,96,97,98,101,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 250,
      "name": "Mohammad Albukheet",
      "letter": "M",
      "date": "2020-04-07T02:18:14.000000Z",
      "moshaf": [
        {
          "id": 250,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/bukheet/",
          "surah_total": 109,
          "moshaf_type": 11,
          "surah_list": "1,2,3,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 251,
      "name": "Nasser Almajed",
      "letter": "N",
      "date": "2020-04-07T02:18:13.000000Z",
      "moshaf": [
        {
          "id": 251,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/nasser_almajed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 252,
      "name": "Ahmed Al-Swailem",
      "letter": "A",
      "date": "2020-04-07T02:18:11.000000Z",
      "moshaf": [
        {
          "id": 252,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/swlim/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 253,
      "name": "Islam Sobhi",
      "letter": "I",
      "date": "2020-04-07T02:18:12.000000Z",
      "moshaf": [
        {
          "id": 253,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server14.mp3quran.net/islam/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 93,
          "moshaf_type": 11,
          "surah_list": "1,2,5,11,12,13,14,15,17,18,19,20,21,23,24,25,26,27,29,30,31,32,34,35,36,38,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,106,107,108,109,110,111,114"
        }
      ]
    },
    {
      "id": 254,
      "name": "Bader Alturki",
      "letter": "B",
      "date": "2020-04-07T02:18:12.000000Z",
      "moshaf": [
        {
          "id": 254,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/bader/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 255,
      "name": "Hitham Aljadani",
      "letter": "H",
      "date": "2020-04-07T02:18:13.000000Z",
      "moshaf": [
        {
          "id": 255,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/hitham/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 38,
          "moshaf_type": 11,
          "surah_list": "1,2,6,7,8,9,10,12,13,14,15,16,28,29,30,31,32,34,35,36,37,38,44,50,51,52,53,54,55,56,57,69,75,76,85,87,88,90"
        }
      ]
    },
    {
      "id": 256,
      "name": "Ahmad Shaheen",
      "letter": "A",
      "date": "2020-04-07T02:18:13.000000Z",
      "moshaf": [
        {
          "id": 256,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/shaheen/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 257,
      "name": "Saad Almqren",
      "letter": "S",
      "date": "2020-04-07T02:18:14.000000Z",
      "moshaf": [
        {
          "id": 257,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/saad/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 259,
      "name": "Ahmad Al Nufais",
      "letter": "A",
      "date": "2023-01-30T15:24:51.000000Z",
      "moshaf": [
        {
          "id": 259,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/nufais/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 26,
      "name": "Rasheed Ifrad",
      "letter": "R",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 26,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server12.mp3quran.net/ifrad/",
          "surah_total": 15,
          "moshaf_type": 21,
          "surah_list": "1,18,25,26,27,28,29,31,33,35,37,38,41,42,71"
        }
      ]
    },
    {
      "id": 260,
      "name": "Omar Al Darweez",
      "letter": "O",
      "date": "2020-05-04T22:45:38.000000Z",
      "moshaf": [
        {
          "id": 260,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/darweez/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 61,
          "moshaf_type": 11,
          "surah_list": "1,12,13,15,18,19,25,32,36,38,44,47,48,50,51,52,53,54,56,61,62,63,64,66,67,68,70,71,72,73,74,75,76,78,79,80,82,85,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 263,
      "name": "Abdulaziz Alasiri",
      "letter": "A",
      "date": "2020-05-04T23:43:58.000000Z",
      "moshaf": [
        {
          "id": 263,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/abdulazizasiri/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 21,
          "moshaf_type": 11,
          "surah_list": "2,3,5,11,12,13,14,17,18,36,45,51,55,57,67,70,71,73,78,86,88"
        }
      ]
    },
    {
      "id": 264,
      "name": "Younes Souilass",
      "letter": "Y",
      "date": "2020-05-25T18:13:32.000000Z",
      "moshaf": [
        {
          "id": 264,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/souilass/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 13,
          "moshaf_type": 21,
          "surah_list": "1,18,19,25,50,51,56,57,67,73,91,97,112"
        }
      ]
    },
    {
      "id": 265,
      "name": "Ahmad Deban",
      "letter": "A",
      "date": "2020-06-16T22:06:00.000000Z",
      "moshaf": [
        {
          "id": 313,
          "name": "Ibn Jammaz A'n Abi Ja'far - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Ibn-Jammaz-A-n-Abi-Ja-far/",
          "surah_total": 11,
          "moshaf_type": 201,
          "surah_list": "1,93,100,102,103,109,110,111,112,113,114"
        },
        {
          "id": 312,
          "name": "Hesham A'n Abi A'mer - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Hesham-A-n-Abi-A-mer/",
          "surah_total": 27,
          "moshaf_type": 191,
          "surah_list": "1,2,3,4,5,6,7,8,9,13,85,90,92,93,94,95,99,100,101,103,105,107,108,110,112,113,114"
        },
        {
          "id": 311,
          "name": "Rewayat Khalaf A'n Hamzah - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Khalaf-A-n-Hamzah/",
          "surah_total": 6,
          "moshaf_type": 31,
          "surah_list": "94,97,101,107,108,109"
        },
        {
          "id": 310,
          "name": "Rewayat AlDorai A'n Al-Kisa'ai - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 13,
          "moshaf_type": 121,
          "surah_list": "1,94,95,100,103,105,106,108,109,110,112,113,114"
        },
        {
          "id": 309,
          "name": "Rewayat Assosi A'n Abi Amr - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Assosi-A-n-Abi-Amr/",
          "surah_total": 19,
          "moshaf_type": 71,
          "surah_list": "1,82,86,87,88,93,94,95,99,102,103,106,108,109,110,111,112,113,114"
        },
        {
          "id": 308,
          "name": "Ibn Thakwan A'n Ibn Amer - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Ibn-Thakwan-A-n-Ibn-Amer/",
          "surah_total": 33,
          "moshaf_type": 161,
          "surah_list": "1,2,3,4,5,6,7,8,9,13,77,83,85,86,88,90,92,93,94,95,96,97,99,100,101,103,105,107,108,109,112,113,114"
        },
        {
          "id": 301,
          "name": "Rewayat Warsh A'n Nafi' Men Tariq Alazraq - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Warsh-A-n-Nafi-Men-Tariq-Alazraq/",
          "surah_total": 114,
          "moshaf_type": 181,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 285,
          "name": "Rewayat Aldori A'n Abi Amr - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Aldori-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 131,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 280,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 279,
          "name": "Rewayat Albizi A'n Ibn Katheer - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Albizi-A-n-Ibn-Katheer/",
          "surah_total": 114,
          "moshaf_type": 41,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 278,
          "name": "Rewayat Qunbol A'n Ibn Katheer - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Qunbol-A-n-Ibn-Katheer/",
          "surah_total": 114,
          "moshaf_type": 61,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 276,
          "name": "Sho'bah A'n Asim - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Sho-bah-A-n-Asim/",
          "surah_total": 114,
          "moshaf_type": 151,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 265,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/deban/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 267,
      "name": "Abdullah Kamel",
      "letter": "A",
      "date": "2020-06-30T21:09:29.000000Z",
      "moshaf": [
        {
          "id": 267,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/kamel/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 268,
      "name": "Peshawa Qadr Al-Kurdi",
      "letter": "P",
      "date": "2020-07-05T10:15:00.000000Z",
      "moshaf": [
        {
          "id": 268,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/peshawa/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 27,
      "name": "Rachid Belalya",
      "letter": "R",
      "date": "2020-04-07T02:17:32.000000Z",
      "moshaf": [
        {
          "id": 261,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/bl3/",
          "surah_total": 5,
          "moshaf_type": 11,
          "surah_list": "46,47,48,49,50"
        },
        {
          "id": 27,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server6.mp3quran.net/bl3/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 271,
      "name": "Nathier Almalki",
      "letter": "N",
      "date": "2020-07-17T17:01:21.000000Z",
      "moshaf": [
        {
          "id": 271,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net//nathier/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 272,
      "name": "Okasha Kameny",
      "letter": "O",
      "date": "2021-01-24T20:32:19.000000Z",
      "moshaf": [
        {
          "id": 296,
          "name": "Rewayat Albizi A'n Ibn Katheer - Murattal",
          "server": "https://server16.mp3quran.net/okasha/Rewayat-Albizi-A-n-Ibn-Katheer/",
          "surah_total": 114,
          "moshaf_type": 41,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 272,
          "name": "Rewayat AlDorai A'n Al-Kisa'ai - Murattal",
          "server": "https://server16.mp3quran.net/okasha/Rewayat-AlDorai-A-n-Al-Kisa-ai/",
          "surah_total": 38,
          "moshaf_type": 121,
          "surah_list": "17,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 273,
      "name": "Haitham Aldukhain",
      "letter": "H",
      "date": "2021-03-25T13:38:35.000000Z",
      "moshaf": [
        {
          "id": 273,
          "name": "Rewayat Hafs A'n Assem - 4",
          "server": "https://server16.mp3quran.net/h_dukhain/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 14,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 274,
      "name": "Muhammad Abu Sneina",
      "letter": "M",
      "date": "2021-03-16T19:38:11.000000Z",
      "moshaf": [
        {
          "id": 274,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/sneineh/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 275,
      "name": "Mohammed Al-Amin Qeniwa",
      "letter": "M",
      "date": "2021-03-18T18:20:44.000000Z",
      "moshaf": [
        {
          "id": 275,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/qeniwa/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 277,
      "name": "Mahmoud Abdul Hakam",
      "letter": "M",
      "date": "2021-04-24T20:07:17.000000Z",
      "moshaf": [
        {
          "id": 277,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/m_abdelhakam/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 113,
          "moshaf_type": 11,
          "surah_list": "1,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 278,
      "name": "Ahmad Issa Al Maasaraawi",
      "letter": "A",
      "date": "2022-05-16T19:26:36.000000Z",
      "moshaf": [
        {
          "id": 290,
          "name": "Rewayat Rowis and Rawh A'n Yakoob Al Hadrami  - Murattal",
          "server": "https://server16.mp3quran.net/a_maasaraawi/Rewayat-Rawh-A-n-Yakoob-Alhadrami/",
          "surah_total": 64,
          "moshaf_type": 91,
          "surah_list": "51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 289,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_maasaraawi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 279,
      "name": "Ibrahim Kshidan",
      "letter": "I",
      "date": "2022-05-23T18:43:01.000000Z",
      "moshaf": [
        {
          "id": 291,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/i_kshidan/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 28,
      "name": "Zakaria Hamamah",
      "letter": "Z",
      "date": "2020-04-07T02:17:33.000000Z",
      "moshaf": [
        {
          "id": 28,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/zakariya/",
          "surah_total": 7,
          "moshaf_type": 11,
          "surah_list": "32,36,44,56,67,76,85"
        }
      ]
    },
    {
      "id": 280,
      "name": "Hashim Abu Dalal",
      "letter": "H",
      "date": "2022-05-25T14:25:53.000000Z",
      "moshaf": [
        {
          "id": 292,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/h_abudalal/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 281,
      "name": "Fouad Alkhamery",
      "letter": "F",
      "date": "2022-05-26T13:35:45.000000Z",
      "moshaf": [
        {
          "id": 293,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/f_khamery/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 282,
      "name": "Sayed Ahmad Hashemi",
      "letter": "S",
      "date": "2022-06-09T13:21:46.000000Z",
      "moshaf": [
        {
          "id": 294,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/s_hashemi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 283,
      "name": "Khalid Mohammadi",
      "letter": "K",
      "date": "2022-06-09T13:40:21.000000Z",
      "moshaf": [
        {
          "id": 295,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/kh_mohammadi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 284,
      "name": "Mal-Allah Abdulrhman Aljaber",
      "letter": "M",
      "date": "2022-08-11T10:41:02.000000Z",
      "moshaf": [
        {
          "id": 297,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/mal-allah_jaber/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 285,
      "name": "Salman Alsadeiq",
      "letter": "S",
      "date": "2022-08-11T13:53:11.000000Z",
      "moshaf": [
        {
          "id": 298,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/s_sadeiq/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 286,
      "name": "Hasan Saleh",
      "letter": "H",
      "date": "2022-08-16T10:28:32.000000Z",
      "moshaf": [
        {
          "id": 299,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/h_saleh/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 287,
      "name": "Abdulrahman Alshahhat",
      "letter": "A",
      "date": "2022-09-02T17:28:53.000000Z",
      "moshaf": [
        {
          "id": 302,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_alshahhat/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 288,
      "name": "Issa Omar Sanankoua",
      "letter": "I",
      "date": "2022-09-10T19:21:58.000000Z",
      "moshaf": [
        {
          "id": 303,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/i_sanankoua/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 26,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,6,12,14,18,20,32,35,40,50,56,57,58,63,67,71,78,87,88,91,112,113,114"
        }
      ]
    },
    {
      "id": 289,
      "name": "Haroon Baqai",
      "letter": "H",
      "date": "2022-11-23T15:10:37.000000Z",
      "moshaf": [
        {
          "id": 304,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/h_baqai/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 51,
          "moshaf_type": 11,
          "surah_list": "1,56,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 29,
      "name": "Abdullah Bukhari",
      "letter": "A",
      "date": "2021-09-17T17:46:33.000000Z",
      "moshaf": [
        {
          "id": 281,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_bukhari/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 80,
          "moshaf_type": 11,
          "surah_list": "1,2,36,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 290,
      "name": "Saleh Alquraishi",
      "letter": "S",
      "date": "2023-10-17T21:16:11.000000Z",
      "moshaf": [
        {
          "id": 306,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/s_alquraishi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 3,
      "name": "Ibrahim Al-Asiri",
      "letter": "I",
      "date": "2020-04-07T02:17:26.000000Z",
      "moshaf": [
        {
          "id": 3,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/3siri/",
          "surah_total": 27,
          "moshaf_type": 11,
          "surah_list": "1,3,4,5,8,12,13,14,17,18,19,20,21,23,27,34,36,38,51,53,54,56,67,69,70,75,76"
        }
      ]
    },
    {
      "id": 30,
      "name": "Saad Al-Ghamdi",
      "letter": "S",
      "date": "2020-04-07T02:17:33.000000Z",
      "moshaf": [
        {
          "id": 30,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server7.mp3quran.net/s_gmd/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 300,
      "name": "Saleh Alshamrani",
      "letter": "S",
      "date": "2022-06-26T19:29:02.000000Z",
      "moshaf": [
        {
          "id": 300,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/shamrani/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 301,
      "name": "Faisal Al-Hajry",
      "letter": "F",
      "date": "2023-01-29T19:24:52.000000Z",
      "moshaf": [
        {
          "id": 307,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/f_hajry/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 302,
      "name": "Anas Alemadi",
      "letter": "A",
      "date": "2023-03-29T20:25:16.000000Z",
      "moshaf": [
        {
          "id": 314,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_alemadi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 303,
      "name": "Abdulmalik Alaskar",
      "letter": "A",
      "date": "2023-04-05T16:21:27.000000Z",
      "moshaf": [
        {
          "id": 315,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_alaskar/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 6,
          "moshaf_type": 11,
          "surah_list": "36,40,69,70,71,75"
        }
      ]
    },
    {
      "id": 304,
      "name": "Abdulkareem Alhazmi",
      "letter": "A",
      "date": "2023-08-12T16:44:36.000000Z",
      "moshaf": [
        {
          "id": 316,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_alhazmi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 305,
      "name": "Hicham Lharraz",
      "letter": "H",
      "date": "2023-08-21T22:20:01.000000Z",
      "moshaf": [
        {
          "id": 317,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/H-Lharraz/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 306,
      "name": "Abdullah Al-Mishal",
      "letter": "A",
      "date": "2023-10-16T23:41:55.000000Z",
      "moshaf": [
        {
          "id": 318,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a-almishal/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 11,
          "moshaf_type": 11,
          "surah_list": "7,14,41,49,50,51,52,53,54,55,56"
        }
      ]
    },
    {
      "id": 307,
      "name": "Abdelaziz sheim",
      "letter": "A",
      "date": "2023-11-06T00:22:23.000000Z",
      "moshaf": [
        {
          "id": 319,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server16.mp3quran.net/a_sheim/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 9,
          "moshaf_type": 21,
          "surah_list": "1,18,31,50,56,67,72,75,112"
        }
      ]
    },
    {
      "id": 31,
      "name": "Saud Al-Shuraim",
      "letter": "S",
      "date": "2020-04-07T02:17:33.000000Z",
      "moshaf": [
        {
          "id": 31,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server7.mp3quran.net/shur/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 32,
      "name": "Sahl Yassin",
      "letter": "S",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 32,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/shl/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 33,
      "name": "Zaki Daghistani",
      "letter": "Z",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 33,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/zaki/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 34,
      "name": "Sami Al-Hasn",
      "letter": "S",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 34,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/sami_hsn/",
          "surah_total": 27,
          "moshaf_type": 11,
          "surah_list": "1,19,20,24,26,27,32,34,55,81,82,86,87,88,91,92,93,94,95,97,102,104,105,109,110,111,112"
        }
      ]
    },
    {
      "id": 35,
      "name": "Sami Al-Dosari",
      "letter": "S",
      "date": "2020-04-07T02:17:34.000000Z",
      "moshaf": [
        {
          "id": 35,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/sami_dosr/",
          "surah_total": 41,
          "moshaf_type": 11,
          "surah_list": "29,30,31,32,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 36,
      "name": "Sayeed Ramadan",
      "letter": "S",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 36,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/sayed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 37,
      "name": "Shaban Al-Sayiaad",
      "letter": "S",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 37,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/shaban/",
          "surah_total": 20,
          "moshaf_type": 11,
          "surah_list": "3,35,87,88,89,90,91,92,94,95,96,97,98,99,100,101,102,103,104,105"
        }
      ]
    },
    {
      "id": 38,
      "name": "Shirazad Taher",
      "letter": "S",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 38,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/taher/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 39,
      "name": "Saber Abdulhakm",
      "letter": "S",
      "date": "2020-04-07T02:17:35.000000Z",
      "moshaf": [
        {
          "id": 39,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/hkm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 4,
      "name": "Shaik Abu Bakr Al Shatri",
      "letter": "S",
      "date": "2020-05-04T23:34:13.000000Z",
      "moshaf": [
        {
          "id": 4,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/shatri/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 40,
      "name": "Saleh Alsahood",
      "letter": "S",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 40,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/sahood/",
          "surah_total": 110,
          "moshaf_type": 11,
          "surah_list": "1,3,4,5,6,7,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 41,
      "name": "Saleh Al-Talib",
      "letter": "S",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 41,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/tlb/",
          "surah_total": 32,
          "moshaf_type": 11,
          "surah_list": "1,25,34,38,39,44,45,46,47,55,56,57,58,59,60,61,70,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86"
        }
      ]
    },
    {
      "id": 42,
      "name": "Saleh Al-Habdan",
      "letter": "S",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 42,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/habdan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 43,
      "name": "Salah Albudair",
      "letter": "S",
      "date": "2020-04-07T02:17:36.000000Z",
      "moshaf": [
        {
          "id": 43,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/s_bud/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 44,
      "name": "Salah Alhashim",
      "letter": "S",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 45,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server12.mp3quran.net/salah_hashim_m/Rewayat-Qalon-A-n-Nafi/",
          "surah_total": 7,
          "moshaf_type": 51,
          "surah_list": "1,12,40,50,53,75,76"
        },
        {
          "id": 44,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/salah_hashim_m/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 46,
      "name": "Slaah Bukhatir",
      "letter": "S",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 46,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/bu_khtr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 47,
      "name": "Mukhtar Al-Haj",
      "letter": "M",
      "date": "2021-11-19T18:59:08.000000Z",
      "moshaf": [
        {
          "id": 283,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/mukhtar_haj/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 16,
          "moshaf_type": 11,
          "surah_list": "1,2,8,12,14,16,18,35,36,41,42,47,55,56,67,68"
        }
      ]
    },
    {
      "id": 48,
      "name": "Adel Ryyan",
      "letter": "A",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 48,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/ryan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 49,
      "name": "Abdelbari Al-Toubayti",
      "letter": "A",
      "date": "2020-04-07T02:17:37.000000Z",
      "moshaf": [
        {
          "id": 49,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/thubti/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 5,
      "name": "Ahmad Al-Ajmy",
      "letter": "A",
      "date": "2020-04-07T02:17:27.000000Z",
      "moshaf": [
        {
          "id": 5,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server10.mp3quran.net/ajm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 50,
      "name": "Abdulbari Mohammad",
      "letter": "A",
      "date": "2020-04-07T02:17:38.000000Z",
      "moshaf": [
        {
          "id": 169,
          "name": "Almusshaf Al Mo'lim - Almusshaf Al Mo'lim",
          "server": "https://server12.mp3quran.net/bari/Almusshaf-Al-Mo-lim/",
          "surah_total": 91,
          "moshaf_type": 213,
          "surah_list": "1,3,5,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 50,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/bari/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 51,
      "name": "Abdulbasit Abdulsamad",
      "letter": "A",
      "date": "2020-06-15T22:50:49.000000Z",
      "moshaf": [
        {
          "id": 53,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server7.mp3quran.net/basit/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 52,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server7.mp3quran.net/basit/Rewayat-Warsh-A-n-Nafi/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 51,
          "name": "Almusshaf Al Mojawwad - Almusshaf Al Mojawwad",
          "server": "https://server7.mp3quran.net/basit/Almusshaf-Al-Mojawwad/",
          "surah_total": 114,
          "moshaf_type": 222,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 54,
      "name": "Abdulrahman Alsudaes",
      "letter": "A",
      "date": "2020-04-07T02:17:38.000000Z",
      "moshaf": [
        {
          "id": 54,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/sds/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 55,
      "name": "Abdul Aziz Al-Ahmad",
      "letter": "A",
      "date": "2020-04-07T02:17:38.000000Z",
      "moshaf": [
        {
          "id": 55,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/a_ahmed/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 56,
      "name": "Abdulaziz Az-Zahrani",
      "letter": "A",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 56,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/zahrani/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 57,
      "name": "Abdullah Al-Burimi",
      "letter": "A",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 57,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/brmi/",
          "surah_total": 41,
          "moshaf_type": 11,
          "surah_list": "1,49,50,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95"
        }
      ]
    },
    {
      "id": 58,
      "name": "Abdullah Albuajan",
      "letter": "A",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 58,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/buajan/",
          "surah_total": 83,
          "moshaf_type": 11,
          "surah_list": "1,8,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,28,29,30,32,33,34,35,39,40,41,42,43,48,49,50,55,56,57,60,62,63,64,65,66,67,68,69,73,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 59,
      "name": "Abdullah Al-Mattrod",
      "letter": "A",
      "date": "2020-04-07T02:17:39.000000Z",
      "moshaf": [
        {
          "id": 59,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/mtrod/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 6,
      "name": "Ahmad Al-Hawashi",
      "letter": "A",
      "date": "2020-04-07T02:17:27.000000Z",
      "moshaf": [
        {
          "id": 6,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/hawashi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 60,
      "name": "Abdullah Basfer",
      "letter": "A",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 60,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/bsfr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 61,
      "name": "Abdullah Khayyat",
      "letter": "A",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 61,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/kyat/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 62,
      "name": "Abdullah Al-Johany",
      "letter": "A",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 62,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server13.mp3quran.net/jhn/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 63,
      "name": "Abdullah Qaulan",
      "letter": "A",
      "date": "2020-04-07T02:17:40.000000Z",
      "moshaf": [
        {
          "id": 63,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/gulan/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 64,
      "name": "Abdulrasheed Soufi",
      "letter": "A",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 258,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/soufi/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 65,
          "name": "Rewayat Assosi A'n Abi Amr - Murattal",
          "server": "https://server16.mp3quran.net/soufi/Rewayat-Assosi-A-n-Abi-Amr/",
          "surah_total": 114,
          "moshaf_type": 71,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 64,
          "name": "Rewayat Khalaf A'n Hamzah - Murattal",
          "server": "https://server16.mp3quran.net/soufi/Rewayat-Khalaf-A-n-Hamzah/",
          "surah_total": 114,
          "moshaf_type": 31,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 66,
      "name": "Abdulmohsin Al-Harthy",
      "letter": "A",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 66,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/mohsin_harthi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 67,
      "name": "Abdulmohsen Al-Qasim",
      "letter": "A",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 67,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/qasm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 68,
      "name": "Abdulmohsin Al-Askar",
      "letter": "A",
      "date": "2020-04-07T02:17:41.000000Z",
      "moshaf": [
        {
          "id": 68,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/askr/",
          "surah_total": 4,
          "moshaf_type": 11,
          "surah_list": "1,2,7,55"
        }
      ]
    },
    {
      "id": 69,
      "name": "Abdulmohsin Al-Obaikan",
      "letter": "A",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 69,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/obk/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 7,
      "name": "Ahmad Saud",
      "letter": "A",
      "date": "2020-04-07T02:17:27.000000Z",
      "moshaf": [
        {
          "id": 7,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/saud/",
          "surah_total": 30,
          "moshaf_type": 11,
          "surah_list": "85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 70,
      "name": "Abdulhadi Kanakeri",
      "letter": "A",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 70,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/kanakeri/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 71,
      "name": "Abdulwadood Haneef",
      "letter": "A",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 71,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/wdod/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 72,
      "name": "Abdulwali Al-Arkani",
      "letter": "A",
      "date": "2020-04-07T02:17:42.000000Z",
      "moshaf": [
        {
          "id": 72,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/arkani/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 73,
      "name": "Ali Abo-Hashim",
      "letter": "A",
      "date": "2020-04-07T02:17:43.000000Z",
      "moshaf": [
        {
          "id": 73,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/abo_hashim/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "50,51,52,53,54,55,56,57"
        }
      ]
    },
    {
      "id": 74,
      "name": "Ali Alhuthaifi",
      "letter": "A",
      "date": "2020-06-17T14:45:14.000000Z",
      "moshaf": [
        {
          "id": 305,
          "name": "Sho'bah A'n Asim - Murattal",
          "server": "https://server9.mp3quran.net/hthfi/Rewayat-Sho-bah-A-n-Asim/",
          "surah_total": 114,
          "moshaf_type": 151,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 75,
          "name": "Rewayat Qalon A'n Nafi' - Murattal",
          "server": "https://server9.mp3quran.net/huthifi_qalon/",
          "surah_total": 114,
          "moshaf_type": 51,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        },
        {
          "id": 74,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/hthfi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 76,
      "name": "Ali Jaber",
      "letter": "A",
      "date": "2020-04-07T02:17:43.000000Z",
      "moshaf": [
        {
          "id": 76,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/a_jbr/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 77,
      "name": "Ali Hajjaj Alsouasi",
      "letter": "A",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 77,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/hajjaj/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 78,
      "name": "Emad Hafez",
      "letter": "E",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 78,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/hafz/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 79,
      "name": "Abdulaziz Alturki",
      "letter": "A",
      "date": "2021-11-16T16:30:45.000000Z",
      "moshaf": [
        {
          "id": 282,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_turki/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 66,
          "moshaf_type": 11,
          "surah_list": "1,2,6,7,8,9,10,11,12,13,18,21,24,25,26,27,28,29,30,31,39,40,41,44,46,48,49,54,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 8,
      "name": "Ahmad Saber",
      "letter": "A",
      "date": "2020-04-07T02:17:28.000000Z",
      "moshaf": [
        {
          "id": 8,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/saber/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 80,
      "name": "Omar Al-Qazabri",
      "letter": "O",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 80,
          "name": "Rewayat Warsh A'n Nafi' - Murattal",
          "server": "https://server9.mp3quran.net/omar_warsh/",
          "surah_total": 114,
          "moshaf_type": 21,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 81,
      "name": "Fares Abbad",
      "letter": "F",
      "date": "2020-04-07T02:17:44.000000Z",
      "moshaf": [
        {
          "id": 81,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/frs_a/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 82,
      "name": "Fahad Al-Otaibi",
      "letter": "F",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 82,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/fahad_otibi/",
          "surah_total": 8,
          "moshaf_type": 11,
          "surah_list": "50,56,69,72,73,74,75,76"
        }
      ]
    },
    {
      "id": 83,
      "name": "Fahad Al-Kandari",
      "letter": "F",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 83,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/kndri/",
          "surah_total": 53,
          "moshaf_type": 11,
          "surah_list": "12,36,51,52,53,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 84,
      "name": "Fawaz Alkabi",
      "letter": "F",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 84,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/fawaz/",
          "surah_total": 44,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,21,22,23,25,27,28,29,30,36,39,40,49,54,55,56,57,58,59,62,63,66,67,73,87,109,112"
        }
      ]
    },
    {
      "id": 85,
      "name": "Lafi Al-Oni",
      "letter": "L",
      "date": "2020-04-07T02:17:45.000000Z",
      "moshaf": [
        {
          "id": 85,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/lafi/",
          "surah_total": 52,
          "moshaf_type": 11,
          "surah_list": "3,12,15,16,19,20,27,28,30,31,32,33,36,37,38,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 86,
      "name": "Nasser Alqatami",
      "letter": "N",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 86,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/qtm/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 87,
      "name": "Nabil Al Rifay",
      "letter": "N",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 87,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/nabil/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 88,
      "name": "Neamah Al-Hassan",
      "letter": "N",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 88,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/namh/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 89,
      "name": "Hani Arrifai",
      "letter": "H",
      "date": "2020-04-07T02:17:46.000000Z",
      "moshaf": [
        {
          "id": 89,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/hani/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 9,
      "name": "Ahmad Nauina",
      "letter": "A",
      "date": "2020-04-07T02:17:28.000000Z",
      "moshaf": [
        {
          "id": 9,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/ahmad_nu/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 90,
      "name": "Walid Al-Dulaimi",
      "letter": "W",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 90,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server8.mp3quran.net/dlami/",
          "surah_total": 51,
          "moshaf_type": 11,
          "surah_list": "1,12,17,31,39,41,45,48,49,50,51,52,53,54,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 91,
      "name": "Waleed Alnaehi",
      "letter": "W",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 91,
          "name": "Rewayat Qalon A'n Nafi' Men Tariq Abi Nasheet - Murattal",
          "server": "https://server9.mp3quran.net/waleed/",
          "surah_total": 114,
          "moshaf_type": 81,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 92,
      "name": "Yasser Al-Dosari",
      "letter": "Y",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 92,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server11.mp3quran.net/yasser/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 93,
      "name": "Yasser Al-Qurashi",
      "letter": "Y",
      "date": "2020-04-07T02:17:47.000000Z",
      "moshaf": [
        {
          "id": 93,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/qurashi/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 94,
      "name": "Yasser Al-Faylakawi",
      "letter": "Y",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 94,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server6.mp3quran.net/fyl/",
          "surah_total": 52,
          "moshaf_type": 11,
          "surah_list": "1,2,25,44,56,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,113,114"
        }
      ]
    },
    {
      "id": 95,
      "name": "Yasser Al-Mazroyee",
      "letter": "Y",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 95,
          "name": "Rewayat Rowis and Rawh A'n Yakoob Al Hadrami  - Murattal",
          "server": "https://server9.mp3quran.net/mzroyee/",
          "surah_total": 114,
          "moshaf_type": 91,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 96,
      "name": "Yahya Hawwa",
      "letter": "Y",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 96,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server12.mp3quran.net/yahya/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 97,
      "name": "Yousef Alshoaey",
      "letter": "Y",
      "date": "2020-04-07T02:17:48.000000Z",
      "moshaf": [
        {
          "id": 97,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server9.mp3quran.net/yousef/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    },
    {
      "id": 98,
      "name": "Abdullah Abdal",
      "letter": "A",
      "date": "2021-11-22T19:47:40.000000Z",
      "moshaf": [
        {
          "id": 284,
          "name": "Rewayat Hafs A'n Assem - Murattal",
          "server": "https://server16.mp3quran.net/a_abdl/Rewayat-Hafs-A-n-Assem/",
          "surah_total": 114,
          "moshaf_type": 11,
          "surah_list": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114"
        }
      ]
    }
  ]

def preprocess_quran_surahs():
    final_data = {}
    for langLists in [(ar_surahs, "ar"), (en_surahs, "en")]:
        surahList,lang = langLists
        for surah in surahList:
            surah_id = surah["id"]
            
            if surah_id not in final_data:
                final_data[surah_id] = {
                    "id": surah["id"],
                    "name": {},
                    "start_page": surah["start_page"],
                    "end_page": surah["end_page"],
                    "makkia": surah["makkia"],
                    "type": surah["type"],
                }
            
            final_data[surah_id]["name"][lang] = surah["name"].strip()

    with open("quran_suwar.json", "w", encoding="utf-8") as file:
        json.dump(final_data, file, indent=4, ensure_ascii=False)

        print("Data has been saved to quran_suwar.json")

def preprocess_moshafs_and_reciters():
    mohafs_final_data = {}
    mohaf_name_to_id = {}
    for langLists in [(ar_mohafs, "ar"), (en_mohafs, "en")]:
        moshafsList,lang = langLists
        for moshaf in moshafsList:
            moshaf_id = moshaf["moshaf_id"]
            moshaf_type = moshaf["moshaf_type"]
            
            if moshaf_id not in mohafs_final_data:
                mohafs_final_data[moshaf_id] = {}
                mohafs_final_data[moshaf_id][moshaf_type] = {}
                mohafs_final_data[moshaf_id][moshaf_type]["name"] = {}
            elif moshaf_type not in mohafs_final_data[moshaf_id]:
                mohafs_final_data[moshaf_id][moshaf_type] = {}
                mohafs_final_data[moshaf_id][moshaf_type]["name"] = {}
            mohafs_final_data[moshaf_id][moshaf_type]["name"][lang] = moshaf["name"].strip()
            mohaf_name_to_id[moshaf["name"].strip()] = (moshaf_id, moshaf_type)
    
    reciters_final_data = {}
    for langLists in [(ar_reciters, "ar"), (en_reciters, "en")]:
        recitersList,lang = langLists
        for reciter in recitersList:
            reciter_id = reciter["id"]
            moshaf_type = moshaf["moshaf_type"]
            if reciter_id not in reciters_final_data:
                reciters_final_data[reciter_id] =     {
                        "id": reciter["id"],
                        "name": {},
                        "letter": {},
                        "date": reciter["date"],
                        "moshaf": []}
                for moshaf in reciter["moshaf"]:
                    if moshaf["name"] in mohaf_name_to_id: 
                        reciters_final_data[reciter_id]["moshaf"].append({
                            "moshaf_id": mohaf_name_to_id[moshaf["name"]][0],
                            "moshaf_type": mohaf_name_to_id[moshaf["name"]][1],
                            "surah_total": moshaf["surah_total"],
                            "server": moshaf["server"],
                            "surah_list": list(map(int, moshaf["surah_list"].split(",")))
                        })
            reciters_final_data[reciter_id]["name"][lang] = reciter["name"]
            reciters_final_data[reciter_id]["letter"][lang] = reciter["letter"]
            
          

    with open("mohafs_final_data.json", "w", encoding="utf-8") as file:
        json.dump(mohafs_final_data, file, indent=4, ensure_ascii=False)
        print("Data has been saved to mohafs_final_data.json")
    with open("reciters_final_data.json", "w", encoding="utf-8") as file:
        json.dump(reciters_final_data, file, indent=4, ensure_ascii=False)
        print("Data has been saved to reciters_final_data.json.json")
import json
from collections import defaultdict


# normalize Arabic letters
def normalize_arabic_text(text: str) -> str:
    replacements = {
        "أ": "ا",
        "إ": "ا",
        "آ": "ا",
        "ٱ": "ا",
        "ى": "ي"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def normalize_arabic_letter(letter: str) -> str:
    return normalize_arabic_text(letter)

# normalize English text (remove dashes)
def normalize_english_text(text: str) -> str:
    return re.sub(r"-", "", text).strip()

# generate all prefix+suffix combinations of words in a name
def generate_search_combs(name: str, normalize: bool = False, lang: str = "ar") -> list[str]:
    if lang == "en":
        name = normalize_english_text(name)

    words = name.split()
    combs = []
    for i in range(len(words)):
        for j in range(i + 1, len(words) + 1):
            chunk = " ".join(words[i:j])
            if normalize and lang == "ar":
                chunk = normalize_arabic_text(chunk)
            combs.append(chunk)
    return combs

def group_reciters_by_letter(input_path: str, output_path: str = "sorted_reciter_names.json") -> None:
    """
    Loads a JSON file of reciters, groups and sorts them by the initial Arabic and English letters of their names.
    Each reciter is represented by a dictionary with 'id', 'name', and 'search_combs'.

    - Normalizes all forms of 'ا' (أ, إ, آ, ٱ → ا) and 'ى' → 'ي'.
    - Removes dashes in English names.
    - Adds 'search_combs' for each reciter containing all prefix/suffix combinations
      of their Arabic (normalized) and English names.

    Args:
        input_path (str): Path to the input JSON file.
        output_path (str): Path where the output JSON will be saved.
    """
    with open(input_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    grouped = {
        "ar": defaultdict(list),
        "en": defaultdict(list)
    }

    for reciter in data.values():
        ar_letter = normalize_arabic_letter(reciter["letter"]["ar"])
        en_letter = reciter["letter"]["en"].upper()

        # generate search combinations (Arabic normalized, English dash-free)
        ar_combs = generate_search_combs(reciter["name"]["ar"], normalize=True, lang="ar")
        en_combs = generate_search_combs(reciter["name"]["en"].lower(), normalize=False, lang="en")

        reciter_entry_ar = {
            "id": reciter["id"],
            "name": reciter["name"]["ar"],
            "search_combs": ar_combs
        }
        reciter_entry_en = {
            "id": reciter["id"],
            "name": reciter["name"]["en"],
            "search_combs": en_combs
        }

        grouped["ar"][ar_letter].append(reciter_entry_ar)
        grouped["en"][en_letter].append(reciter_entry_en)

    # Sort groups by letter and then by name
    grouped["ar"] = {
        k: sorted(v, key=lambda x: normalize_arabic_text(x["name"])) for k, v in sorted(grouped["ar"].items())
    }
    grouped["en"] = {
        k: sorted(v, key=lambda x: x["name"]) for k, v in sorted(grouped["en"].items())
    }

    with open(output_path, "w", encoding="utf-8") as out_file:
        json.dump(grouped, out_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    group_reciters_by_letter("src/data/quranmp3/reciters.json")
