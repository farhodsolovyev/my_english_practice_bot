"""1000 популярных английских слов (принцип Парето 80/20).
Автогенерация: перевод + IPA + русская транскрипция. Источник: 1000word.xlsx."""

WORDS = [
  {
    "id": 1,
    "english": "a",
    "transcription": "ə",
    "ru": "э",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "неопр. артикль"
      }
    ]
  },
  {
    "id": 2,
    "english": "able",
    "transcription": "ˈeɪbl",
    "ru": "эйбл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "способный"
      }
    ]
  },
  {
    "id": 3,
    "english": "about",
    "transcription": "əˈbaʊt",
    "ru": "эбаут",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "о/около"
      }
    ]
  },
  {
    "id": 4,
    "english": "above",
    "transcription": "əˈbʌv",
    "ru": "эбав",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "над"
      }
    ]
  },
  {
    "id": 5,
    "english": "accept",
    "transcription": "əkˈsept",
    "ru": "эксэпт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "принимать"
      }
    ]
  },
  {
    "id": 6,
    "english": "across",
    "transcription": "əˈkrɒs",
    "ru": "экрос",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "через"
      }
    ]
  },
  {
    "id": 7,
    "english": "act",
    "transcription": "ækt",
    "ru": "экт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "действовать"
      }
    ]
  },
  {
    "id": 8,
    "english": "actually",
    "transcription": "ˈæktʃuəli",
    "ru": "экчуэли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "на самом деле"
      }
    ]
  },
  {
    "id": 9,
    "english": "add",
    "transcription": "æd",
    "ru": "эд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "добавлять"
      }
    ]
  },
  {
    "id": 10,
    "english": "admit",
    "transcription": "ədˈmɪt",
    "ru": "эдмит",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "признавать"
      }
    ]
  },
  {
    "id": 11,
    "english": "afraid",
    "transcription": "əˈfreɪd",
    "ru": "эфрэйд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "испуганный"
      }
    ]
  },
  {
    "id": 12,
    "english": "after",
    "transcription": "ˈɑːftə",
    "ru": "афтэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "после"
      }
    ]
  },
  {
    "id": 13,
    "english": "afternoon",
    "transcription": "ˌɑːftəˈnuːn",
    "ru": "афтэнун",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "день"
      }
    ]
  },
  {
    "id": 14,
    "english": "again",
    "transcription": "əˈɡen",
    "ru": "эгэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "снова"
      }
    ]
  },
  {
    "id": 15,
    "english": "against",
    "transcription": "əˈɡenst",
    "ru": "эгэнст",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "против"
      }
    ]
  },
  {
    "id": 16,
    "english": "age",
    "transcription": "eɪdʒ",
    "ru": "эйдж",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "возраст"
      }
    ]
  },
  {
    "id": 17,
    "english": "ago",
    "transcription": "əˈɡəʊ",
    "ru": "эгоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "назад"
      }
    ]
  },
  {
    "id": 18,
    "english": "agree",
    "transcription": "əˈɡriː",
    "ru": "эгри",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "соглашаться"
      }
    ]
  },
  {
    "id": 19,
    "english": "ah",
    "transcription": "ɑː",
    "ru": "а",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ах"
      }
    ]
  },
  {
    "id": 20,
    "english": "ahead",
    "transcription": "əˈhed",
    "ru": "эхэд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "впереди"
      }
    ]
  },
  {
    "id": 21,
    "english": "air",
    "transcription": "eə",
    "ru": "эа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "воздух"
      }
    ]
  },
  {
    "id": 22,
    "english": "all",
    "transcription": "ɔːl",
    "ru": "ол",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "весь/все"
      }
    ]
  },
  {
    "id": 23,
    "english": "allow",
    "transcription": "əˈlaʊ",
    "ru": "элау",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "позволять"
      }
    ]
  },
  {
    "id": 24,
    "english": "almost",
    "transcription": "ˈɔːlməʊst",
    "ru": "олмоуст",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "почти"
      }
    ]
  },
  {
    "id": 25,
    "english": "alone",
    "transcription": "əˈləʊn",
    "ru": "элоун",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "один"
      }
    ]
  },
  {
    "id": 26,
    "english": "along",
    "transcription": "əˈlɒŋ",
    "ru": "элон",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вдоль"
      }
    ]
  },
  {
    "id": 27,
    "english": "already",
    "transcription": "ɔːlˈredi",
    "ru": "олрэди",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "уже"
      }
    ]
  },
  {
    "id": 28,
    "english": "alright",
    "transcription": "ɔːlˈraɪt",
    "ru": "олрайт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "хорошо"
      }
    ]
  },
  {
    "id": 29,
    "english": "also",
    "transcription": "ˈɔːlsəʊ",
    "ru": "олсоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "также"
      }
    ]
  },
  {
    "id": 30,
    "english": "although",
    "transcription": "ɔːlˈðəʊ",
    "ru": "олзоу",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хотя"
      }
    ]
  },
  {
    "id": 31,
    "english": "always",
    "transcription": "ˈɔːlweɪz",
    "ru": "олвэйз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "всегда"
      }
    ]
  },
  {
    "id": 32,
    "english": "am",
    "transcription": "æm",
    "ru": "эм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "есть (быть)"
      }
    ]
  },
  {
    "id": 33,
    "english": "amaze",
    "transcription": "əˈmeɪz",
    "ru": "эмэйз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "изумлять"
      }
    ]
  },
  {
    "id": 34,
    "english": "an",
    "transcription": "ən",
    "ru": "эн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "неопр. артикль"
      }
    ]
  },
  {
    "id": 35,
    "english": "and",
    "transcription": "ænd",
    "ru": "энд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "и"
      }
    ]
  },
  {
    "id": 36,
    "english": "anger",
    "transcription": "ˈæŋɡə",
    "ru": "энгэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "гнев"
      }
    ]
  },
  {
    "id": 37,
    "english": "angry",
    "transcription": "ˈæŋɡri",
    "ru": "энгри",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сердитый"
      }
    ]
  },
  {
    "id": 38,
    "english": "animal",
    "transcription": "ˈænɪml",
    "ru": "энимл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "животное"
      }
    ]
  },
  {
    "id": 39,
    "english": "annoy",
    "transcription": "əˈnɔɪ",
    "ru": "эной",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "раздражать"
      }
    ]
  },
  {
    "id": 40,
    "english": "another",
    "transcription": "əˈnʌðə",
    "ru": "эназэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "другой"
      }
    ]
  },
  {
    "id": 41,
    "english": "answer",
    "transcription": "ˈɑːnsə",
    "ru": "ансэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ответ"
      }
    ]
  },
  {
    "id": 42,
    "english": "any",
    "transcription": "ˈeni",
    "ru": "эни",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "любой"
      }
    ]
  },
  {
    "id": 43,
    "english": "anymore",
    "transcription": "ˌeniˈmɔː",
    "ru": "энимо",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "больше не"
      }
    ]
  },
  {
    "id": 44,
    "english": "anyone",
    "transcription": "ˈeniwʌn",
    "ru": "эниуан",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кто-нибудь"
      }
    ]
  },
  {
    "id": 45,
    "english": "anything",
    "transcription": "ˈeniθɪŋ",
    "ru": "энисин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "что-нибудь"
      }
    ]
  },
  {
    "id": 46,
    "english": "anyway",
    "transcription": "ˈeniweɪ",
    "ru": "энивэй",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "в любом случае"
      }
    ]
  },
  {
    "id": 47,
    "english": "apartment",
    "transcription": "əˈpɑːtmənt",
    "ru": "эпатмэнт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "квартира"
      }
    ]
  },
  {
    "id": 48,
    "english": "apparently",
    "transcription": "əˈpærəntli",
    "ru": "эпэрэнтли",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "по-видимому"
      }
    ]
  },
  {
    "id": 49,
    "english": "appear",
    "transcription": "əˈpɪə",
    "ru": "эпиэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "появляться"
      }
    ]
  },
  {
    "id": 50,
    "english": "approach",
    "transcription": "əˈprəʊtʃ",
    "ru": "эпроуч",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "подход"
      }
    ]
  },
  {
    "id": 51,
    "english": "are",
    "transcription": "ɑː",
    "ru": "а",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "есть (быть)"
      }
    ]
  },
  {
    "id": 52,
    "english": "area",
    "transcription": "ˈeəriə",
    "ru": "эариэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "область"
      }
    ]
  },
  {
    "id": 53,
    "english": "aren't",
    "transcription": "ɑːnt",
    "ru": "ант",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не есть"
      }
    ]
  },
  {
    "id": 54,
    "english": "arm",
    "transcription": "ɑːm",
    "ru": "ам",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рука"
      }
    ]
  },
  {
    "id": 55,
    "english": "around",
    "transcription": "əˈraʊnd",
    "ru": "эраунд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вокруг"
      }
    ]
  },
  {
    "id": 56,
    "english": "arrive",
    "transcription": "əˈraɪv",
    "ru": "эрайв",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "прибывать"
      }
    ]
  },
  {
    "id": 57,
    "english": "as",
    "transcription": "æz",
    "ru": "эз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "как"
      }
    ]
  },
  {
    "id": 58,
    "english": "ask",
    "transcription": "ɑːsk",
    "ru": "аск",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "спрашивать"
      }
    ]
  },
  {
    "id": 59,
    "english": "asleep",
    "transcription": "əˈsliːp",
    "ru": "эслип",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "спящий"
      }
    ]
  },
  {
    "id": 60,
    "english": "ass",
    "transcription": "æs",
    "ru": "эс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "задница"
      }
    ]
  },
  {
    "id": 61,
    "english": "at",
    "transcription": "æt",
    "ru": "эт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "в/на"
      }
    ]
  },
  {
    "id": 62,
    "english": "attack",
    "transcription": "əˈtæk",
    "ru": "этэк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "атака"
      }
    ]
  },
  {
    "id": 63,
    "english": "attempt",
    "transcription": "əˈtempt",
    "ru": "этэмпт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "попытка"
      }
    ]
  },
  {
    "id": 64,
    "english": "attention",
    "transcription": "əˈtenʃn",
    "ru": "этэншн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "внимание"
      }
    ]
  },
  {
    "id": 65,
    "english": "aunt",
    "transcription": "ɑːnt",
    "ru": "ант",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тётя"
      }
    ]
  },
  {
    "id": 66,
    "english": "avoid",
    "transcription": "əˈvɔɪd",
    "ru": "эвойд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "избегать"
      }
    ]
  },
  {
    "id": 67,
    "english": "away",
    "transcription": "əˈweɪ",
    "ru": "эвэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "прочь"
      }
    ]
  },
  {
    "id": 68,
    "english": "baby",
    "transcription": "ˈbeɪbi",
    "ru": "бэйби",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "младенец"
      }
    ]
  },
  {
    "id": 69,
    "english": "back",
    "transcription": "bæk",
    "ru": "бэк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "назад/спина"
      }
    ]
  },
  {
    "id": 70,
    "english": "bad",
    "transcription": "bæd",
    "ru": "бэд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "плохой"
      }
    ]
  },
  {
    "id": 71,
    "english": "bag",
    "transcription": "bæɡ",
    "ru": "бэг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сумка"
      }
    ]
  },
  {
    "id": 72,
    "english": "ball",
    "transcription": "bɔːl",
    "ru": "бол",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мяч"
      }
    ]
  },
  {
    "id": 73,
    "english": "band",
    "transcription": "bænd",
    "ru": "бэнд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "группа"
      }
    ]
  },
  {
    "id": 74,
    "english": "bar",
    "transcription": "bɑː",
    "ru": "ба",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бар"
      }
    ]
  },
  {
    "id": 75,
    "english": "barely",
    "transcription": "ˈbeəli",
    "ru": "бэали",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "едва"
      }
    ]
  },
  {
    "id": 76,
    "english": "bathroom",
    "transcription": "ˈbɑːθruːm",
    "ru": "басрум",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ванная"
      }
    ]
  },
  {
    "id": 77,
    "english": "be",
    "transcription": "biː",
    "ru": "би",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "быть"
      }
    ]
  },
  {
    "id": 78,
    "english": "beat",
    "transcription": "biːt",
    "ru": "бит",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бить"
      }
    ]
  },
  {
    "id": 79,
    "english": "beautiful",
    "transcription": "ˈbjuːtɪfl",
    "ru": "бьютифл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "красивый"
      }
    ]
  },
  {
    "id": 80,
    "english": "became",
    "transcription": "bɪˈkeɪm",
    "ru": "бикэйм",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "стал"
      }
    ]
  },
  {
    "id": 81,
    "english": "because",
    "transcription": "bɪˈkɒz",
    "ru": "бикоз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "потому что"
      }
    ]
  },
  {
    "id": 82,
    "english": "become",
    "transcription": "bɪˈkʌm",
    "ru": "бикам",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "становиться"
      }
    ]
  },
  {
    "id": 83,
    "english": "bed",
    "transcription": "bed",
    "ru": "бэд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кровать"
      }
    ]
  },
  {
    "id": 84,
    "english": "bedroom",
    "transcription": "ˈbedruːm",
    "ru": "бэдрум",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "спальня"
      }
    ]
  },
  {
    "id": 85,
    "english": "been",
    "transcription": "biːn",
    "ru": "бин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "был (быть)"
      }
    ]
  },
  {
    "id": 86,
    "english": "before",
    "transcription": "bɪˈfɔː",
    "ru": "бифо",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "до/перед"
      }
    ]
  },
  {
    "id": 87,
    "english": "began",
    "transcription": "bɪˈɡæn",
    "ru": "бигэн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "начал"
      }
    ]
  },
  {
    "id": 88,
    "english": "begin",
    "transcription": "bɪˈɡɪn",
    "ru": "бигин",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "начинать"
      }
    ]
  },
  {
    "id": 89,
    "english": "behind",
    "transcription": "bɪˈhaɪnd",
    "ru": "бихайнд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "позади"
      }
    ]
  },
  {
    "id": 90,
    "english": "believe",
    "transcription": "bɪˈliːv",
    "ru": "билив",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "верить"
      }
    ]
  },
  {
    "id": 91,
    "english": "bell",
    "transcription": "bel",
    "ru": "бэл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "колокол"
      }
    ]
  },
  {
    "id": 92,
    "english": "beside",
    "transcription": "bɪˈsaɪd",
    "ru": "бисайд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рядом"
      }
    ]
  },
  {
    "id": 93,
    "english": "besides",
    "transcription": "bɪˈsaɪdz",
    "ru": "бисайдз",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кроме того"
      }
    ]
  },
  {
    "id": 94,
    "english": "best",
    "transcription": "best",
    "ru": "бэст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "лучший"
      }
    ]
  },
  {
    "id": 95,
    "english": "better",
    "transcription": "ˈbetə",
    "ru": "бэтэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "лучше"
      }
    ]
  },
  {
    "id": 96,
    "english": "between",
    "transcription": "bɪˈtwiːn",
    "ru": "битуин",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "между"
      }
    ]
  },
  {
    "id": 97,
    "english": "big",
    "transcription": "bɪɡ",
    "ru": "биг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "большой"
      }
    ]
  },
  {
    "id": 98,
    "english": "bit",
    "transcription": "bɪt",
    "ru": "бит",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "немного"
      }
    ]
  },
  {
    "id": 99,
    "english": "bite",
    "transcription": "baɪt",
    "ru": "байт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кусать"
      }
    ]
  },
  {
    "id": 100,
    "english": "black",
    "transcription": "blæk",
    "ru": "блэк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "чёрный"
      }
    ]
  },
  {
    "id": 101,
    "english": "blink",
    "transcription": "blɪŋk",
    "ru": "блинк",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "моргать"
      }
    ]
  },
  {
    "id": 102,
    "english": "block",
    "transcription": "blɒk",
    "ru": "блок",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "блок"
      }
    ]
  },
  {
    "id": 103,
    "english": "blonde",
    "transcription": "blɒnd",
    "ru": "блонд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "блондинка"
      }
    ]
  },
  {
    "id": 104,
    "english": "blood",
    "transcription": "blʌd",
    "ru": "блад",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кровь"
      }
    ]
  },
  {
    "id": 105,
    "english": "blue",
    "transcription": "bluː",
    "ru": "блу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "синий"
      }
    ]
  },
  {
    "id": 106,
    "english": "blush",
    "transcription": "blʌʃ",
    "ru": "блаш",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "краснеть"
      }
    ]
  },
  {
    "id": 107,
    "english": "body",
    "transcription": "ˈbɒdi",
    "ru": "боди",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тело"
      }
    ]
  },
  {
    "id": 108,
    "english": "book",
    "transcription": "bʊk",
    "ru": "бук",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "книга"
      }
    ]
  },
  {
    "id": 109,
    "english": "bore",
    "transcription": "bɔː",
    "ru": "бо",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "наскучить"
      }
    ]
  },
  {
    "id": 110,
    "english": "both",
    "transcription": "bəʊθ",
    "ru": "боус",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "оба"
      }
    ]
  },
  {
    "id": 111,
    "english": "bother",
    "transcription": "ˈbɒðə",
    "ru": "бозэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "беспокоить"
      }
    ]
  },
  {
    "id": 112,
    "english": "bottle",
    "transcription": "ˈbɒtl",
    "ru": "ботл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "бутылка"
      }
    ]
  },
  {
    "id": 113,
    "english": "bottom",
    "transcription": "ˈbɒtəm",
    "ru": "ботэм",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "низ"
      }
    ]
  },
  {
    "id": 114,
    "english": "box",
    "transcription": "bɒks",
    "ru": "бокс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "коробка"
      }
    ]
  },
  {
    "id": 115,
    "english": "boy",
    "transcription": "bɔɪ",
    "ru": "бой",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мальчик"
      }
    ]
  },
  {
    "id": 116,
    "english": "boyfriend",
    "transcription": "ˈbɔɪfrend",
    "ru": "бойфренд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "парень"
      }
    ]
  },
  {
    "id": 117,
    "english": "brain",
    "transcription": "breɪn",
    "ru": "брейн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мозг"
      }
    ]
  },
  {
    "id": 118,
    "english": "break",
    "transcription": "breɪk",
    "ru": "брейк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ломать"
      }
    ]
  },
  {
    "id": 119,
    "english": "breakfast",
    "transcription": "ˈbrekfəst",
    "ru": "брекфэст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "завтрак"
      }
    ]
  },
  {
    "id": 120,
    "english": "breath",
    "transcription": "breθ",
    "ru": "брес",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дыхание"
      }
    ]
  },
  {
    "id": 121,
    "english": "breathe",
    "transcription": "briːð",
    "ru": "бриз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дышать"
      }
    ]
  },
  {
    "id": 122,
    "english": "bright",
    "transcription": "braɪt",
    "ru": "брайт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "яркий"
      }
    ]
  },
  {
    "id": 123,
    "english": "bring",
    "transcription": "brɪŋ",
    "ru": "бринг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "приносить"
      }
    ]
  },
  {
    "id": 124,
    "english": "broke",
    "transcription": "brəʊk",
    "ru": "броук",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сломал"
      }
    ]
  },
  {
    "id": 125,
    "english": "broken",
    "transcription": "ˈbrəʊkən",
    "ru": "броукэн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сломанный"
      }
    ]
  },
  {
    "id": 126,
    "english": "brother",
    "transcription": "ˈbrʌðə",
    "ru": "бразэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "брат"
      }
    ]
  },
  {
    "id": 127,
    "english": "brought",
    "transcription": "brɔːt",
    "ru": "брот",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "принёс"
      }
    ]
  },
  {
    "id": 128,
    "english": "brown",
    "transcription": "braʊn",
    "ru": "браун",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "коричневый"
      }
    ]
  },
  {
    "id": 129,
    "english": "brush",
    "transcription": "brʌʃ",
    "ru": "браш",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "щётка"
      }
    ]
  },
  {
    "id": 130,
    "english": "build",
    "transcription": "bɪld",
    "ru": "билд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "строить"
      }
    ]
  },
  {
    "id": 131,
    "english": "burn",
    "transcription": "bɜːn",
    "ru": "бён",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "гореть"
      }
    ]
  },
  {
    "id": 132,
    "english": "burst",
    "transcription": "bɜːst",
    "ru": "бёст",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "лопнуть"
      }
    ]
  },
  {
    "id": 133,
    "english": "bus",
    "transcription": "bʌs",
    "ru": "бас",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "автобус"
      }
    ]
  },
  {
    "id": 134,
    "english": "business",
    "transcription": "ˈbɪznəs",
    "ru": "бизнэс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бизнес"
      }
    ]
  },
  {
    "id": 135,
    "english": "busy",
    "transcription": "ˈbɪzi",
    "ru": "бизи",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "занятой"
      }
    ]
  },
  {
    "id": 136,
    "english": "but",
    "transcription": "bʌt",
    "ru": "бат",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "но"
      }
    ]
  },
  {
    "id": 137,
    "english": "buy",
    "transcription": "baɪ",
    "ru": "бай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "покупать"
      }
    ]
  },
  {
    "id": 138,
    "english": "by",
    "transcription": "baɪ",
    "ru": "бай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "у, рядом"
      }
    ]
  },
  {
    "id": 139,
    "english": "call",
    "transcription": "kɔːl",
    "ru": "кол",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "звать"
      }
    ]
  },
  {
    "id": 140,
    "english": "calm",
    "transcription": "kɑːm",
    "ru": "кам",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "спокойный"
      }
    ]
  },
  {
    "id": 141,
    "english": "came",
    "transcription": "keɪm",
    "ru": "кейм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пришёл"
      }
    ]
  },
  {
    "id": 142,
    "english": "can",
    "transcription": "kæn",
    "ru": "кэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мочь"
      }
    ]
  },
  {
    "id": 143,
    "english": "can't",
    "transcription": "kɑːnt",
    "ru": "кант",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не может"
      }
    ]
  },
  {
    "id": 144,
    "english": "car",
    "transcription": "kɑː",
    "ru": "ка",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "машина"
      }
    ]
  },
  {
    "id": 145,
    "english": "card",
    "transcription": "kɑːd",
    "ru": "кад",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "карта"
      }
    ]
  },
  {
    "id": 146,
    "english": "care",
    "transcription": "keə",
    "ru": "кэа",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "забота"
      }
    ]
  },
  {
    "id": 147,
    "english": "carefully",
    "transcription": "ˈkeəfli",
    "ru": "кэафли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "осторожно"
      }
    ]
  },
  {
    "id": 148,
    "english": "carry",
    "transcription": "ˈkæri",
    "ru": "кэри",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "нести"
      }
    ]
  },
  {
    "id": 149,
    "english": "case",
    "transcription": "keɪs",
    "ru": "кейс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "случай"
      }
    ]
  },
  {
    "id": 150,
    "english": "cat",
    "transcription": "kæt",
    "ru": "кэт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кошка"
      }
    ]
  },
  {
    "id": 151,
    "english": "catch",
    "transcription": "kætʃ",
    "ru": "кэтч",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ловить"
      }
    ]
  },
  {
    "id": 152,
    "english": "caught",
    "transcription": "kɔːt",
    "ru": "кот",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "поймал"
      }
    ]
  },
  {
    "id": 153,
    "english": "cause",
    "transcription": "kɔːz",
    "ru": "коз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "причина"
      }
    ]
  },
  {
    "id": 154,
    "english": "cell",
    "transcription": "sel",
    "ru": "сэл",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "клетка"
      }
    ]
  },
  {
    "id": 155,
    "english": "chair",
    "transcription": "tʃeə",
    "ru": "чэа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "стул"
      }
    ]
  },
  {
    "id": 156,
    "english": "chance",
    "transcription": "tʃɑːns",
    "ru": "чанс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "шанс"
      }
    ]
  },
  {
    "id": 157,
    "english": "change",
    "transcription": "tʃeɪndʒ",
    "ru": "чейндж",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "менять"
      }
    ]
  },
  {
    "id": 158,
    "english": "chase",
    "transcription": "tʃeɪs",
    "ru": "чейс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "преследовать"
      }
    ]
  },
  {
    "id": 159,
    "english": "check",
    "transcription": "tʃek",
    "ru": "чек",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "проверять"
      }
    ]
  },
  {
    "id": 160,
    "english": "cheek",
    "transcription": "tʃiːk",
    "ru": "чик",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "щека"
      }
    ]
  },
  {
    "id": 161,
    "english": "chest",
    "transcription": "tʃest",
    "ru": "чест",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "грудь"
      }
    ]
  },
  {
    "id": 162,
    "english": "child",
    "transcription": "tʃaɪld",
    "ru": "чайлд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ребёнок"
      }
    ]
  },
  {
    "id": 163,
    "english": "children",
    "transcription": "ˈtʃɪldrən",
    "ru": "чилдрэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дети"
      }
    ]
  },
  {
    "id": 164,
    "english": "chuckle",
    "transcription": "ˈtʃʌkl",
    "ru": "чакл",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "усмехаться"
      }
    ]
  },
  {
    "id": 165,
    "english": "city",
    "transcription": "ˈsɪti",
    "ru": "сити",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "город"
      }
    ]
  },
  {
    "id": 166,
    "english": "class",
    "transcription": "klɑːs",
    "ru": "клас",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "класс"
      }
    ]
  },
  {
    "id": 167,
    "english": "clean",
    "transcription": "kliːn",
    "ru": "клин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "чистый"
      }
    ]
  },
  {
    "id": 168,
    "english": "clear",
    "transcription": "klɪə",
    "ru": "клиэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ясный"
      }
    ]
  },
  {
    "id": 169,
    "english": "climb",
    "transcription": "klaɪm",
    "ru": "клайм",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "взбираться"
      }
    ]
  },
  {
    "id": 170,
    "english": "close",
    "transcription": "kləʊz",
    "ru": "клоуз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "закрывать"
      }
    ]
  },
  {
    "id": 171,
    "english": "clothes",
    "transcription": "kləʊðz",
    "ru": "клоузз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "одежда"
      }
    ]
  },
  {
    "id": 172,
    "english": "coffee",
    "transcription": "ˈkɒfi",
    "ru": "кофи",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кофе"
      }
    ]
  },
  {
    "id": 173,
    "english": "cold",
    "transcription": "kəʊld",
    "ru": "коулд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "холодный"
      }
    ]
  },
  {
    "id": 174,
    "english": "college",
    "transcription": "ˈkɒlɪdʒ",
    "ru": "колидж",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "колледж"
      }
    ]
  },
  {
    "id": 175,
    "english": "color",
    "transcription": "ˈkʌlə",
    "ru": "калэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "цвет"
      }
    ]
  },
  {
    "id": 176,
    "english": "come",
    "transcription": "kʌm",
    "ru": "кам",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "приходить"
      }
    ]
  },
  {
    "id": 177,
    "english": "comment",
    "transcription": "ˈkɒment",
    "ru": "комэнт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "комментарий"
      }
    ]
  },
  {
    "id": 178,
    "english": "complete",
    "transcription": "kəmˈpliːt",
    "ru": "кэмплит",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "полный"
      }
    ]
  },
  {
    "id": 179,
    "english": "completely",
    "transcription": "kəmˈpliːtli",
    "ru": "кэмплитли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "полностью"
      }
    ]
  },
  {
    "id": 180,
    "english": "computer",
    "transcription": "kəmˈpjuːtə",
    "ru": "кэмпьютэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "компьютер"
      }
    ]
  },
  {
    "id": 181,
    "english": "concern",
    "transcription": "kənˈsɜːn",
    "ru": "кэнсён",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "беспокойство"
      }
    ]
  },
  {
    "id": 182,
    "english": "confuse",
    "transcription": "kənˈfjuːz",
    "ru": "кэнфьюз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "путать"
      }
    ]
  },
  {
    "id": 183,
    "english": "consider",
    "transcription": "kənˈsɪdə",
    "ru": "кэнсидэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рассматривать"
      }
    ]
  },
  {
    "id": 184,
    "english": "continue",
    "transcription": "kənˈtɪnjuː",
    "ru": "кэнтинью",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "продолжать"
      }
    ]
  },
  {
    "id": 185,
    "english": "control",
    "transcription": "kənˈtrəʊl",
    "ru": "кэнтроул",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "контроль"
      }
    ]
  },
  {
    "id": 186,
    "english": "conversation",
    "transcription": "ˌkɒnvəˈseɪʃn",
    "ru": "конвэсейшн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "разговор"
      }
    ]
  },
  {
    "id": 187,
    "english": "cool",
    "transcription": "kuːl",
    "ru": "кул",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "прохладный"
      }
    ]
  },
  {
    "id": 188,
    "english": "corner",
    "transcription": "ˈkɔːnə",
    "ru": "конэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "угол"
      }
    ]
  },
  {
    "id": 189,
    "english": "couch",
    "transcription": "kaʊtʃ",
    "ru": "кауч",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "диван"
      }
    ]
  },
  {
    "id": 190,
    "english": "could",
    "transcription": "kʊd",
    "ru": "куд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мог"
      }
    ]
  },
  {
    "id": 191,
    "english": "couldn't",
    "transcription": "ˈkʊdnt",
    "ru": "куднт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не мог"
      }
    ]
  },
  {
    "id": 192,
    "english": "counter",
    "transcription": "ˈkaʊntə",
    "ru": "каунтэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "прилавок"
      }
    ]
  },
  {
    "id": 193,
    "english": "couple",
    "transcription": "ˈkʌpl",
    "ru": "капл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пара"
      }
    ]
  },
  {
    "id": 194,
    "english": "course",
    "transcription": "kɔːs",
    "ru": "кос",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "курс"
      }
    ]
  },
  {
    "id": 195,
    "english": "cover",
    "transcription": "ˈkʌvə",
    "ru": "кавэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "покрывать"
      }
    ]
  },
  {
    "id": 196,
    "english": "crack",
    "transcription": "kræk",
    "ru": "крэк",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "трещина"
      }
    ]
  },
  {
    "id": 197,
    "english": "crazy",
    "transcription": "ˈkreɪzi",
    "ru": "крейзи",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сумасшедший"
      }
    ]
  },
  {
    "id": 198,
    "english": "cross",
    "transcription": "krɒs",
    "ru": "крос",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пересекать"
      }
    ]
  },
  {
    "id": 199,
    "english": "crowd",
    "transcription": "kraʊd",
    "ru": "крауд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "толпа"
      }
    ]
  },
  {
    "id": 200,
    "english": "cry",
    "transcription": "kraɪ",
    "ru": "край",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "плакать"
      }
    ]
  },
  {
    "id": 201,
    "english": "cup",
    "transcription": "kʌp",
    "ru": "кап",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "чашка"
      }
    ]
  },
  {
    "id": 202,
    "english": "cut",
    "transcription": "kʌt",
    "ru": "кат",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "резать"
      }
    ]
  },
  {
    "id": 203,
    "english": "cute",
    "transcription": "kjuːt",
    "ru": "кьют",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "милый"
      }
    ]
  },
  {
    "id": 204,
    "english": "dad",
    "transcription": "dæd",
    "ru": "дэд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "папа"
      }
    ]
  },
  {
    "id": 205,
    "english": "damn",
    "transcription": "dæm",
    "ru": "дэм",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "проклятый"
      }
    ]
  },
  {
    "id": 206,
    "english": "dance",
    "transcription": "dɑːns",
    "ru": "данс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "танцевать"
      }
    ]
  },
  {
    "id": 207,
    "english": "dark",
    "transcription": "dɑːk",
    "ru": "дак",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тёмный"
      }
    ]
  },
  {
    "id": 208,
    "english": "date",
    "transcription": "deɪt",
    "ru": "дэйт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дата"
      }
    ]
  },
  {
    "id": 209,
    "english": "daughter",
    "transcription": "ˈdɔːtə",
    "ru": "доте",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дочь"
      }
    ]
  },
  {
    "id": 210,
    "english": "day",
    "transcription": "deɪ",
    "ru": "дэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "день"
      }
    ]
  },
  {
    "id": 211,
    "english": "dead",
    "transcription": "ded",
    "ru": "дэд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мёртвый"
      }
    ]
  },
  {
    "id": 212,
    "english": "deal",
    "transcription": "diːl",
    "ru": "дил",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сделка"
      }
    ]
  },
  {
    "id": 213,
    "english": "dear",
    "transcription": "dɪə",
    "ru": "диэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "дорогой"
      }
    ]
  },
  {
    "id": 214,
    "english": "death",
    "transcription": "deθ",
    "ru": "дэс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "смерть"
      }
    ]
  },
  {
    "id": 215,
    "english": "decide",
    "transcription": "dɪˈsaɪd",
    "ru": "дисайд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "решать"
      }
    ]
  },
  {
    "id": 216,
    "english": "deep",
    "transcription": "diːp",
    "ru": "дип",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "глубокий"
      }
    ]
  },
  {
    "id": 217,
    "english": "definitely",
    "transcription": "ˈdefɪnətli",
    "ru": "дэфинитли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "определённо"
      }
    ]
  },
  {
    "id": 218,
    "english": "desk",
    "transcription": "desk",
    "ru": "дэск",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "стол"
      }
    ]
  },
  {
    "id": 219,
    "english": "did",
    "transcription": "dɪd",
    "ru": "дид",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "делал"
      }
    ]
  },
  {
    "id": 220,
    "english": "didn't",
    "transcription": "ˈdɪdnt",
    "ru": "диднт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не делал"
      }
    ]
  },
  {
    "id": 221,
    "english": "die",
    "transcription": "daɪ",
    "ru": "дай",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "умирать"
      }
    ]
  },
  {
    "id": 222,
    "english": "different",
    "transcription": "ˈdɪfrənt",
    "ru": "дифрэнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "разный"
      }
    ]
  },
  {
    "id": 223,
    "english": "dinner",
    "transcription": "ˈdɪnə",
    "ru": "динэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ужин"
      }
    ]
  },
  {
    "id": 224,
    "english": "direction",
    "transcription": "dɪˈrekʃn",
    "ru": "дирэкшн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "направление"
      }
    ]
  },
  {
    "id": 225,
    "english": "disappear",
    "transcription": "ˌdɪsəˈpɪə",
    "ru": "дисэпиэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "исчезать"
      }
    ]
  },
  {
    "id": 226,
    "english": "do",
    "transcription": "duː",
    "ru": "ду",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "делать"
      }
    ]
  },
  {
    "id": 227,
    "english": "doctor",
    "transcription": "ˈdɒktə",
    "ru": "доктэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "врач"
      }
    ]
  },
  {
    "id": 228,
    "english": "does",
    "transcription": "dʌz",
    "ru": "даз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "делает"
      }
    ]
  },
  {
    "id": 229,
    "english": "doesn't",
    "transcription": "ˈdʌznt",
    "ru": "дазнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не делает"
      }
    ]
  },
  {
    "id": 230,
    "english": "dog",
    "transcription": "dɒg",
    "ru": "дог",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "собака"
      }
    ]
  },
  {
    "id": 231,
    "english": "don't",
    "transcription": "dəʊnt",
    "ru": "доунт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не делать"
      }
    ]
  },
  {
    "id": 232,
    "english": "done",
    "transcription": "dʌn",
    "ru": "дан",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сделанный"
      }
    ]
  },
  {
    "id": 233,
    "english": "door",
    "transcription": "dɔː",
    "ru": "до",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дверь"
      }
    ]
  },
  {
    "id": 234,
    "english": "doubt",
    "transcription": "daʊt",
    "ru": "даут",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сомнение"
      }
    ]
  },
  {
    "id": 235,
    "english": "down",
    "transcription": "daʊn",
    "ru": "даун",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вниз"
      }
    ]
  },
  {
    "id": 236,
    "english": "drag",
    "transcription": "dræg",
    "ru": "дрэг",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тащить"
      }
    ]
  },
  {
    "id": 237,
    "english": "draw",
    "transcription": "drɔː",
    "ru": "дро",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рисовать"
      }
    ]
  },
  {
    "id": 238,
    "english": "dream",
    "transcription": "driːm",
    "ru": "дрим",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мечта"
      }
    ]
  },
  {
    "id": 239,
    "english": "dress",
    "transcription": "dres",
    "ru": "дрэс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "платье"
      }
    ]
  },
  {
    "id": 240,
    "english": "drink",
    "transcription": "drɪŋk",
    "ru": "дринк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пить"
      }
    ]
  },
  {
    "id": 241,
    "english": "drive",
    "transcription": "draɪv",
    "ru": "драйв",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "водить"
      }
    ]
  },
  {
    "id": 242,
    "english": "drop",
    "transcription": "drɒp",
    "ru": "дроп",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ронять"
      }
    ]
  },
  {
    "id": 243,
    "english": "drove",
    "transcription": "drəʊv",
    "ru": "дроув",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вёл"
      }
    ]
  },
  {
    "id": 244,
    "english": "dry",
    "transcription": "draɪ",
    "ru": "драй",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сухой"
      }
    ]
  },
  {
    "id": 245,
    "english": "during",
    "transcription": "ˈdjʊərɪŋ",
    "ru": "дьюэринг",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "во время"
      }
    ]
  },
  {
    "id": 246,
    "english": "each",
    "transcription": "iːtʃ",
    "ru": "ич",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "каждый"
      }
    ]
  },
  {
    "id": 247,
    "english": "ear",
    "transcription": "ɪə",
    "ru": "иэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ухо"
      }
    ]
  },
  {
    "id": 248,
    "english": "early",
    "transcription": "ˈɜːli",
    "ru": "ёли",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рано"
      }
    ]
  },
  {
    "id": 249,
    "english": "easily",
    "transcription": "ˈiːzɪli",
    "ru": "изили",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "легко"
      }
    ]
  },
  {
    "id": 250,
    "english": "easy",
    "transcription": "ˈiːzi",
    "ru": "изи",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "лёгкий"
      }
    ]
  },
  {
    "id": 251,
    "english": "eat",
    "transcription": "iːt",
    "ru": "ит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "есть"
      }
    ]
  },
  {
    "id": 252,
    "english": "edge",
    "transcription": "edʒ",
    "ru": "эдж",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "край"
      }
    ]
  },
  {
    "id": 253,
    "english": "either",
    "transcription": "ˈaɪðə",
    "ru": "айзэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "любой"
      }
    ]
  },
  {
    "id": 254,
    "english": "else",
    "transcription": "els",
    "ru": "элс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ещё"
      }
    ]
  },
  {
    "id": 255,
    "english": "empty",
    "transcription": "ˈempti",
    "ru": "эмпти",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пустой"
      }
    ]
  },
  {
    "id": 256,
    "english": "end",
    "transcription": "end",
    "ru": "энд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "конец"
      }
    ]
  },
  {
    "id": 257,
    "english": "enjoy",
    "transcription": "ɪnˈdʒɔɪ",
    "ru": "инджой",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "наслаждаться"
      }
    ]
  },
  {
    "id": 258,
    "english": "enough",
    "transcription": "ɪˈnʌf",
    "ru": "инаф",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "достаточно"
      }
    ]
  },
  {
    "id": 259,
    "english": "enter",
    "transcription": "ˈentə",
    "ru": "энтэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "входить"
      }
    ]
  },
  {
    "id": 260,
    "english": "entire",
    "transcription": "ɪnˈtaɪə",
    "ru": "интайэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "весь"
      }
    ]
  },
  {
    "id": 261,
    "english": "escape",
    "transcription": "ɪˈskeɪp",
    "ru": "искэйп",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "побег"
      }
    ]
  },
  {
    "id": 262,
    "english": "especially",
    "transcription": "ɪˈspeʃəli",
    "ru": "испэшэли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "особенно"
      }
    ]
  },
  {
    "id": 263,
    "english": "even",
    "transcription": "ˈiːvn",
    "ru": "ивн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "даже"
      }
    ]
  },
  {
    "id": 264,
    "english": "evening",
    "transcription": "ˈiːvnɪŋ",
    "ru": "ивнинг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вечер"
      }
    ]
  },
  {
    "id": 265,
    "english": "eventually",
    "transcription": "ɪˈventʃuəli",
    "ru": "ивэнчуэли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "в конце концов"
      }
    ]
  },
  {
    "id": 266,
    "english": "ever",
    "transcription": "ˈevə",
    "ru": "эвэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "когда-либо"
      }
    ]
  },
  {
    "id": 267,
    "english": "every",
    "transcription": "ˈevri",
    "ru": "эври",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "каждый"
      }
    ]
  },
  {
    "id": 268,
    "english": "everyone",
    "transcription": "ˈevriwʌn",
    "ru": "эвриуан",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "все"
      }
    ]
  },
  {
    "id": 269,
    "english": "everything",
    "transcription": "ˈevriθɪŋ",
    "ru": "эврисинг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "всё"
      }
    ]
  },
  {
    "id": 270,
    "english": "exactly",
    "transcription": "ɪgˈzæktli",
    "ru": "игзэктли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "точно"
      }
    ]
  },
  {
    "id": 271,
    "english": "except",
    "transcription": "ɪkˈsept",
    "ru": "иксэпт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кроме"
      }
    ]
  },
  {
    "id": 272,
    "english": "excite",
    "transcription": "ɪkˈsaɪt",
    "ru": "иксайт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "волновать"
      }
    ]
  },
  {
    "id": 273,
    "english": "exclaim",
    "transcription": "ɪkˈskleɪm",
    "ru": "иксклэйм",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "восклицать"
      }
    ]
  },
  {
    "id": 274,
    "english": "excuse",
    "transcription": "ɪkˈskjuːs",
    "ru": "икскьюс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "извинять"
      }
    ]
  },
  {
    "id": 275,
    "english": "expect",
    "transcription": "ɪkˈspekt",
    "ru": "икспэкт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ожидать"
      }
    ]
  },
  {
    "id": 276,
    "english": "explain",
    "transcription": "ɪkˈspleɪn",
    "ru": "иксплэйн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "объяснять"
      }
    ]
  },
  {
    "id": 277,
    "english": "expression",
    "transcription": "ɪkˈspreʃn",
    "ru": "икспрэшн",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "выражение"
      }
    ]
  },
  {
    "id": 278,
    "english": "eye",
    "transcription": "aɪ",
    "ru": "ай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "глаз"
      }
    ]
  },
  {
    "id": 279,
    "english": "eyebrow",
    "transcription": "ˈaɪbraʊ",
    "ru": "айбрау",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "бровь"
      }
    ]
  },
  {
    "id": 280,
    "english": "face",
    "transcription": "feɪs",
    "ru": "фэйс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "лицо"
      }
    ]
  },
  {
    "id": 281,
    "english": "fact",
    "transcription": "fækt",
    "ru": "фэкт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "факт"
      }
    ]
  },
  {
    "id": 282,
    "english": "fall",
    "transcription": "fɔːl",
    "ru": "фол",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "падать"
      }
    ]
  },
  {
    "id": 283,
    "english": "family",
    "transcription": "ˈfæməli",
    "ru": "фэмили",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "семья"
      }
    ]
  },
  {
    "id": 284,
    "english": "far",
    "transcription": "fɑː",
    "ru": "фа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "далеко"
      }
    ]
  },
  {
    "id": 285,
    "english": "fast",
    "transcription": "fɑːst",
    "ru": "фаст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "быстрый"
      }
    ]
  },
  {
    "id": 286,
    "english": "father",
    "transcription": "ˈfɑːðə",
    "ru": "фазэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "отец"
      }
    ]
  },
  {
    "id": 287,
    "english": "fault",
    "transcription": "fɔːlt",
    "ru": "фолт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вина"
      }
    ]
  },
  {
    "id": 288,
    "english": "favorite",
    "transcription": "ˈfeɪvərɪt",
    "ru": "фэйвэрит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "любимый"
      }
    ]
  },
  {
    "id": 289,
    "english": "fear",
    "transcription": "fɪə",
    "ru": "фиэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "страх"
      }
    ]
  },
  {
    "id": 290,
    "english": "feel",
    "transcription": "fiːl",
    "ru": "фил",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "чувствовать"
      }
    ]
  },
  {
    "id": 291,
    "english": "feet",
    "transcription": "fiːt",
    "ru": "фит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ноги"
      }
    ]
  },
  {
    "id": 292,
    "english": "fell",
    "transcription": "fel",
    "ru": "фэл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "упал"
      }
    ]
  },
  {
    "id": 293,
    "english": "felt",
    "transcription": "felt",
    "ru": "фэлт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "чувствовал"
      }
    ]
  },
  {
    "id": 294,
    "english": "few",
    "transcription": "fjuː",
    "ru": "фью",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "немного"
      }
    ]
  },
  {
    "id": 295,
    "english": "field",
    "transcription": "fiːld",
    "ru": "филд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "поле"
      }
    ]
  },
  {
    "id": 296,
    "english": "fight",
    "transcription": "faɪt",
    "ru": "файт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "драться"
      }
    ]
  },
  {
    "id": 297,
    "english": "figure",
    "transcription": "ˈfɪgə",
    "ru": "фигэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "фигура"
      }
    ]
  },
  {
    "id": 298,
    "english": "fill",
    "transcription": "fɪl",
    "ru": "фил",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "наполнять"
      }
    ]
  },
  {
    "id": 299,
    "english": "finally",
    "transcription": "ˈfaɪnəli",
    "ru": "файнэли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "наконец"
      }
    ]
  },
  {
    "id": 300,
    "english": "find",
    "transcription": "faɪnd",
    "ru": "файнд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "находить"
      }
    ]
  },
  {
    "id": 301,
    "english": "fine",
    "transcription": "faɪn",
    "ru": "файн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хорошо"
      }
    ]
  },
  {
    "id": 302,
    "english": "finger",
    "transcription": "ˈfɪŋɡə",
    "ru": "фингэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "палец"
      }
    ]
  },
  {
    "id": 303,
    "english": "finish",
    "transcription": "ˈfɪnɪʃ",
    "ru": "финиш",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "закончить"
      }
    ]
  },
  {
    "id": 304,
    "english": "fire",
    "transcription": "ˈfaɪə",
    "ru": "файэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "огонь"
      }
    ]
  },
  {
    "id": 305,
    "english": "first",
    "transcription": "fɜːst",
    "ru": "фёст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "первый"
      }
    ]
  },
  {
    "id": 306,
    "english": "fit",
    "transcription": "fɪt",
    "ru": "фит",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "подходить"
      }
    ]
  },
  {
    "id": 307,
    "english": "five",
    "transcription": "faɪv",
    "ru": "файв",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пять"
      }
    ]
  },
  {
    "id": 308,
    "english": "fix",
    "transcription": "fɪks",
    "ru": "фикс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "чинить"
      }
    ]
  },
  {
    "id": 309,
    "english": "flash",
    "transcription": "flæʃ",
    "ru": "флэш",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вспышка"
      }
    ]
  },
  {
    "id": 310,
    "english": "flip",
    "transcription": "flɪp",
    "ru": "флип",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "переворачивать"
      }
    ]
  },
  {
    "id": 311,
    "english": "floor",
    "transcription": "flɔː",
    "ru": "флор",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пол"
      }
    ]
  },
  {
    "id": 312,
    "english": "fly",
    "transcription": "flaɪ",
    "ru": "флай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "летать"
      }
    ]
  },
  {
    "id": 313,
    "english": "focus",
    "transcription": "ˈfəʊkəs",
    "ru": "фоукэс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "фокус"
      }
    ]
  },
  {
    "id": 314,
    "english": "follow",
    "transcription": "ˈfɒləʊ",
    "ru": "фолоу",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "следовать"
      }
    ]
  },
  {
    "id": 315,
    "english": "food",
    "transcription": "fuːd",
    "ru": "фуд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "еда"
      }
    ]
  },
  {
    "id": 316,
    "english": "foot",
    "transcription": "fʊt",
    "ru": "фут",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нога"
      }
    ]
  },
  {
    "id": 317,
    "english": "for",
    "transcription": "fɔː",
    "ru": "фо",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "для"
      }
    ]
  },
  {
    "id": 318,
    "english": "force",
    "transcription": "fɔːs",
    "ru": "форс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сила"
      }
    ]
  },
  {
    "id": 319,
    "english": "forget",
    "transcription": "fəˈɡet",
    "ru": "фэгет",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "забывать"
      }
    ]
  },
  {
    "id": 320,
    "english": "form",
    "transcription": "fɔːm",
    "ru": "форм",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "форма"
      }
    ]
  },
  {
    "id": 321,
    "english": "forward",
    "transcription": "ˈfɔːwəd",
    "ru": "форуэд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вперёд"
      }
    ]
  },
  {
    "id": 322,
    "english": "found",
    "transcription": "faʊnd",
    "ru": "фаунд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нашёл"
      }
    ]
  },
  {
    "id": 323,
    "english": "four",
    "transcription": "fɔː",
    "ru": "фо",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "четыре"
      }
    ]
  },
  {
    "id": 324,
    "english": "free",
    "transcription": "friː",
    "ru": "фри",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "свободный"
      }
    ]
  },
  {
    "id": 325,
    "english": "friend",
    "transcription": "frend",
    "ru": "френд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "друг"
      }
    ]
  },
  {
    "id": 326,
    "english": "from",
    "transcription": "frɒm",
    "ru": "фром",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "из"
      }
    ]
  },
  {
    "id": 327,
    "english": "front",
    "transcription": "frʌnt",
    "ru": "франт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "перед"
      }
    ]
  },
  {
    "id": 328,
    "english": "frown",
    "transcription": "fraʊn",
    "ru": "фраун",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "хмуриться"
      }
    ]
  },
  {
    "id": 329,
    "english": "fuck",
    "transcription": "fʌk",
    "ru": "фак",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "грубое ругательство"
      }
    ]
  },
  {
    "id": 330,
    "english": "full",
    "transcription": "fʊl",
    "ru": "фул",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "полный"
      }
    ]
  },
  {
    "id": 331,
    "english": "fun",
    "transcription": "fʌn",
    "ru": "фан",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "веселье"
      }
    ]
  },
  {
    "id": 332,
    "english": "funny",
    "transcription": "ˈfʌni",
    "ru": "фани",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "смешной"
      }
    ]
  },
  {
    "id": 333,
    "english": "further",
    "transcription": "ˈfɜːðə",
    "ru": "фёзэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дальше"
      }
    ]
  },
  {
    "id": 334,
    "english": "game",
    "transcription": "ɡeɪm",
    "ru": "гейм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "игра"
      }
    ]
  },
  {
    "id": 335,
    "english": "gasp",
    "transcription": "ɡɑːsp",
    "ru": "гасп",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ахнуть"
      }
    ]
  },
  {
    "id": 336,
    "english": "gave",
    "transcription": "ɡeɪv",
    "ru": "гейв",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дал"
      }
    ]
  },
  {
    "id": 337,
    "english": "gaze",
    "transcription": "ɡeɪz",
    "ru": "гейз",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пристальный взгляд"
      }
    ]
  },
  {
    "id": 338,
    "english": "gently",
    "transcription": "ˈdʒentli",
    "ru": "джентли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нежно"
      }
    ]
  },
  {
    "id": 339,
    "english": "get",
    "transcription": "ɡet",
    "ru": "гет",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "получать"
      }
    ]
  },
  {
    "id": 340,
    "english": "giggle",
    "transcription": "ˈɡɪɡl",
    "ru": "гигл",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "хихикать"
      }
    ]
  },
  {
    "id": 341,
    "english": "girl",
    "transcription": "ɡɜːl",
    "ru": "гёл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "девочка"
      }
    ]
  },
  {
    "id": 342,
    "english": "girlfriend",
    "transcription": "ˈɡɜːlfrend",
    "ru": "гёлфренд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "девушка"
      }
    ]
  },
  {
    "id": 343,
    "english": "give",
    "transcription": "ɡɪv",
    "ru": "гив",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "давать"
      }
    ]
  },
  {
    "id": 344,
    "english": "given",
    "transcription": "ˈɡɪvn",
    "ru": "гивн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "данный"
      }
    ]
  },
  {
    "id": 345,
    "english": "glad",
    "transcription": "ɡlæd",
    "ru": "глэд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "рад"
      }
    ]
  },
  {
    "id": 346,
    "english": "glance",
    "transcription": "ɡlɑːns",
    "ru": "гланс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "взгляд"
      }
    ]
  },
  {
    "id": 347,
    "english": "glare",
    "transcription": "ɡleə",
    "ru": "глэа",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сердитый взгляд"
      }
    ]
  },
  {
    "id": 348,
    "english": "glass",
    "transcription": "ɡlɑːs",
    "ru": "глас",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "стекло"
      }
    ]
  },
  {
    "id": 349,
    "english": "go",
    "transcription": "ɡəʊ",
    "ru": "гоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "идти"
      }
    ]
  },
  {
    "id": 350,
    "english": "god",
    "transcription": "ɡɒd",
    "ru": "год",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "бог"
      }
    ]
  },
  {
    "id": 351,
    "english": "gone",
    "transcription": "ɡɒn",
    "ru": "гон",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ушёл"
      }
    ]
  },
  {
    "id": 352,
    "english": "gonna",
    "transcription": "ˈɡɒnə",
    "ru": "гонэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "собираться"
      }
    ]
  },
  {
    "id": 353,
    "english": "good",
    "transcription": "ɡʊd",
    "ru": "гуд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хороший"
      }
    ]
  },
  {
    "id": 354,
    "english": "got",
    "transcription": "ɡɒt",
    "ru": "гот",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "получил"
      }
    ]
  },
  {
    "id": 355,
    "english": "gotten",
    "transcription": "ˈɡɒtn",
    "ru": "готн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "получил"
      }
    ]
  },
  {
    "id": 356,
    "english": "grab",
    "transcription": "ɡræb",
    "ru": "грэб",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хватать"
      }
    ]
  },
  {
    "id": 357,
    "english": "great",
    "transcription": "ɡreɪt",
    "ru": "грейт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "великий"
      }
    ]
  },
  {
    "id": 358,
    "english": "green",
    "transcription": "ɡriːn",
    "ru": "грин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "зелёный"
      }
    ]
  },
  {
    "id": 359,
    "english": "greet",
    "transcription": "ɡriːt",
    "ru": "грит",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "приветствовать"
      }
    ]
  },
  {
    "id": 360,
    "english": "grey",
    "transcription": "ɡreɪ",
    "ru": "грей",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "серый"
      }
    ]
  },
  {
    "id": 361,
    "english": "grin",
    "transcription": "ɡrɪn",
    "ru": "грин",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ухмылка"
      }
    ]
  },
  {
    "id": 362,
    "english": "grip",
    "transcription": "ɡrɪp",
    "ru": "грип",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "хватка"
      }
    ]
  },
  {
    "id": 363,
    "english": "groan",
    "transcription": "ɡrəʊn",
    "ru": "гроун",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "стон"
      }
    ]
  },
  {
    "id": 364,
    "english": "ground",
    "transcription": "ɡraʊnd",
    "ru": "граунд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "земля"
      }
    ]
  },
  {
    "id": 365,
    "english": "group",
    "transcription": "ɡruːp",
    "ru": "груп",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "группа"
      }
    ]
  },
  {
    "id": 366,
    "english": "grow",
    "transcription": "ɡrəʊ",
    "ru": "гроу",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "расти"
      }
    ]
  },
  {
    "id": 367,
    "english": "guard",
    "transcription": "ɡɑːd",
    "ru": "гад",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "охрана"
      }
    ]
  },
  {
    "id": 368,
    "english": "guess",
    "transcription": "ɡes",
    "ru": "гес",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "угадать"
      }
    ]
  },
  {
    "id": 369,
    "english": "gun",
    "transcription": "ɡʌn",
    "ru": "ган",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пистолет"
      }
    ]
  },
  {
    "id": 370,
    "english": "guy",
    "transcription": "ɡaɪ",
    "ru": "гай",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "парень"
      }
    ]
  },
  {
    "id": 371,
    "english": "had",
    "transcription": "hæd",
    "ru": "хэд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "имел"
      }
    ]
  },
  {
    "id": 372,
    "english": "hadn't",
    "transcription": "ˈhædnt",
    "ru": "хэднт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "не имел"
      }
    ]
  },
  {
    "id": 373,
    "english": "hair",
    "transcription": "heə",
    "ru": "хэа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "волосы"
      }
    ]
  },
  {
    "id": 374,
    "english": "half",
    "transcription": "hɑːf",
    "ru": "хаф",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "половина"
      }
    ]
  },
  {
    "id": 375,
    "english": "hall",
    "transcription": "hɔːl",
    "ru": "хол",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "зал"
      }
    ]
  },
  {
    "id": 376,
    "english": "hallway",
    "transcription": "ˈhɔːlweɪ",
    "ru": "холуэй",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "коридор"
      }
    ]
  },
  {
    "id": 377,
    "english": "hand",
    "transcription": "hænd",
    "ru": "хэнд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рука"
      }
    ]
  },
  {
    "id": 378,
    "english": "handle",
    "transcription": "ˈhændl",
    "ru": "хэндл",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "справляться"
      }
    ]
  },
  {
    "id": 379,
    "english": "hang",
    "transcription": "hæŋ",
    "ru": "хэнг",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "висеть"
      }
    ]
  },
  {
    "id": 380,
    "english": "happen",
    "transcription": "ˈhæpən",
    "ru": "хэпэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "случаться"
      }
    ]
  },
  {
    "id": 381,
    "english": "happy",
    "transcription": "ˈhæpi",
    "ru": "хэпи",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "счастливый"
      }
    ]
  },
  {
    "id": 382,
    "english": "hard",
    "transcription": "hɑːd",
    "ru": "хад",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "трудный"
      }
    ]
  },
  {
    "id": 383,
    "english": "has",
    "transcription": "hæz",
    "ru": "хэз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "имеет"
      }
    ]
  },
  {
    "id": 384,
    "english": "hate",
    "transcription": "heɪt",
    "ru": "хейт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ненавидеть"
      }
    ]
  },
  {
    "id": 385,
    "english": "have",
    "transcription": "hæv",
    "ru": "хэв",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "иметь"
      }
    ]
  },
  {
    "id": 386,
    "english": "haven't",
    "transcription": "ˈhævnt",
    "ru": "хэвнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не имею"
      }
    ]
  },
  {
    "id": 387,
    "english": "he",
    "transcription": "hiː",
    "ru": "хи",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "он"
      }
    ]
  },
  {
    "id": 388,
    "english": "he'd",
    "transcription": "hiːd",
    "ru": "хид",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "он бы"
      }
    ]
  },
  {
    "id": 389,
    "english": "he's",
    "transcription": "hiːz",
    "ru": "хиз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "он есть"
      }
    ]
  },
  {
    "id": 390,
    "english": "head",
    "transcription": "hed",
    "ru": "хэд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "голова"
      }
    ]
  },
  {
    "id": 391,
    "english": "hear",
    "transcription": "hɪə",
    "ru": "хиэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "слышать"
      }
    ]
  },
  {
    "id": 392,
    "english": "heard",
    "transcription": "hɜːd",
    "ru": "хёд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "слышал"
      }
    ]
  },
  {
    "id": 393,
    "english": "heart",
    "transcription": "hɑːt",
    "ru": "хат",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сердце"
      }
    ]
  },
  {
    "id": 394,
    "english": "heavy",
    "transcription": "ˈhevi",
    "ru": "хэви",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тяжёлый"
      }
    ]
  },
  {
    "id": 395,
    "english": "held",
    "transcription": "held",
    "ru": "хэлд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "держал"
      }
    ]
  },
  {
    "id": 396,
    "english": "hell",
    "transcription": "hel",
    "ru": "хэл",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ад"
      }
    ]
  },
  {
    "id": 397,
    "english": "hello",
    "transcription": "həˈləʊ",
    "ru": "хэлоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "привет"
      }
    ]
  },
  {
    "id": 398,
    "english": "help",
    "transcription": "help",
    "ru": "хэлп",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "помощь"
      }
    ]
  },
  {
    "id": 399,
    "english": "her",
    "transcription": "hɜː",
    "ru": "хё",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "её"
      }
    ]
  },
  {
    "id": 400,
    "english": "here",
    "transcription": "hɪə",
    "ru": "хиэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "здесь"
      }
    ]
  },
  {
    "id": 401,
    "english": "herself",
    "transcription": "hɜːˈself",
    "ru": "хёсэлф",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "себя"
      }
    ]
  },
  {
    "id": 402,
    "english": "hey",
    "transcription": "heɪ",
    "ru": "хэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "эй"
      }
    ]
  },
  {
    "id": 403,
    "english": "hi",
    "transcription": "haɪ",
    "ru": "хай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "привет"
      }
    ]
  },
  {
    "id": 404,
    "english": "hide",
    "transcription": "haɪd",
    "ru": "хайд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "прятать"
      }
    ]
  },
  {
    "id": 405,
    "english": "high",
    "transcription": "haɪ",
    "ru": "хай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "высокий"
      }
    ]
  },
  {
    "id": 406,
    "english": "him",
    "transcription": "hɪm",
    "ru": "хим",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "его"
      }
    ]
  },
  {
    "id": 407,
    "english": "himself",
    "transcription": "hɪmˈself",
    "ru": "химсэлф",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сам"
      }
    ]
  },
  {
    "id": 408,
    "english": "his",
    "transcription": "hɪz",
    "ru": "хиз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "его"
      }
    ]
  },
  {
    "id": 409,
    "english": "hit",
    "transcription": "hɪt",
    "ru": "хит",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ударить"
      }
    ]
  },
  {
    "id": 410,
    "english": "hold",
    "transcription": "həʊld",
    "ru": "хоулд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "держать"
      }
    ]
  },
  {
    "id": 411,
    "english": "home",
    "transcription": "həʊm",
    "ru": "хоум",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дом"
      }
    ]
  },
  {
    "id": 412,
    "english": "hope",
    "transcription": "həʊp",
    "ru": "хоуп",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "надеяться"
      }
    ]
  },
  {
    "id": 413,
    "english": "horse",
    "transcription": "hɔːs",
    "ru": "хос",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "лошадь"
      }
    ]
  },
  {
    "id": 414,
    "english": "hospital",
    "transcription": "ˈhɒspɪtl",
    "ru": "хоспитл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "больница"
      }
    ]
  },
  {
    "id": 415,
    "english": "hot",
    "transcription": "hɒt",
    "ru": "хот",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "горячий"
      }
    ]
  },
  {
    "id": 416,
    "english": "hour",
    "transcription": "ˈaʊə",
    "ru": "ауэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "час"
      }
    ]
  },
  {
    "id": 417,
    "english": "house",
    "transcription": "haʊs",
    "ru": "хаус",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дом"
      }
    ]
  },
  {
    "id": 418,
    "english": "how",
    "transcription": "haʊ",
    "ru": "хау",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "как"
      }
    ]
  },
  {
    "id": 419,
    "english": "however",
    "transcription": "haʊˈevə",
    "ru": "хауэвэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "однако"
      }
    ]
  },
  {
    "id": 420,
    "english": "hug",
    "transcription": "hʌɡ",
    "ru": "хаг",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "обнимать"
      }
    ]
  },
  {
    "id": 421,
    "english": "huge",
    "transcription": "hjuːdʒ",
    "ru": "хьюдж",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "огромный"
      }
    ]
  },
  {
    "id": 422,
    "english": "huh",
    "transcription": "hʌ",
    "ru": "ха",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "а?"
      }
    ]
  },
  {
    "id": 423,
    "english": "human",
    "transcription": "ˈhjuːmən",
    "ru": "хьюмэн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "человек"
      }
    ]
  },
  {
    "id": 424,
    "english": "hundred",
    "transcription": "ˈhʌndrəd",
    "ru": "хандрэд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сто"
      }
    ]
  },
  {
    "id": 425,
    "english": "hung",
    "transcription": "hʌŋ",
    "ru": "ханг",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "повесил"
      }
    ]
  },
  {
    "id": 426,
    "english": "hurry",
    "transcription": "ˈhʌri",
    "ru": "хари",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "торопиться"
      }
    ]
  },
  {
    "id": 427,
    "english": "hurt",
    "transcription": "hɜːt",
    "ru": "хёт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "болеть"
      }
    ]
  },
  {
    "id": 428,
    "english": "i",
    "transcription": "aɪ",
    "ru": "ай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "я"
      }
    ]
  },
  {
    "id": 429,
    "english": "i'd",
    "transcription": "aɪd",
    "ru": "айд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "я бы"
      }
    ]
  },
  {
    "id": 430,
    "english": "i'll",
    "transcription": "aɪl",
    "ru": "айл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "я буду"
      }
    ]
  },
  {
    "id": 431,
    "english": "i'm",
    "transcription": "aɪm",
    "ru": "айм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "я есть"
      }
    ]
  },
  {
    "id": 432,
    "english": "i've",
    "transcription": "aɪv",
    "ru": "айв",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "я имею"
      }
    ]
  },
  {
    "id": 433,
    "english": "ice",
    "transcription": "aɪs",
    "ru": "айс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "лёд"
      }
    ]
  },
  {
    "id": 434,
    "english": "idea",
    "transcription": "aɪˈdɪə",
    "ru": "айдиэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "идея"
      }
    ]
  },
  {
    "id": 435,
    "english": "if",
    "transcription": "ɪf",
    "ru": "иф",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "если"
      }
    ]
  },
  {
    "id": 436,
    "english": "ignore",
    "transcription": "ɪɡˈnɔː",
    "ru": "игно",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "игнорировать"
      }
    ]
  },
  {
    "id": 437,
    "english": "imagine",
    "transcription": "ɪˈmædʒɪn",
    "ru": "имэджин",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "воображать"
      }
    ]
  },
  {
    "id": 438,
    "english": "immediately",
    "transcription": "ɪˈmiːdiətli",
    "ru": "имидиэтли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "немедленно"
      }
    ]
  },
  {
    "id": 439,
    "english": "important",
    "transcription": "ɪmˈpɔːtnt",
    "ru": "импотнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "важный"
      }
    ]
  },
  {
    "id": 440,
    "english": "in",
    "transcription": "ɪn",
    "ru": "ин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "в"
      }
    ]
  },
  {
    "id": 441,
    "english": "inside",
    "transcription": "ɪnˈsaɪd",
    "ru": "инсайд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "внутри"
      }
    ]
  },
  {
    "id": 442,
    "english": "instead",
    "transcription": "ɪnˈsted",
    "ru": "инстэд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вместо"
      }
    ]
  },
  {
    "id": 443,
    "english": "interest",
    "transcription": "ˈɪntrəst",
    "ru": "интрэст",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "интерес"
      }
    ]
  },
  {
    "id": 444,
    "english": "interrupt",
    "transcription": "ˌɪntəˈrʌpt",
    "ru": "интэрапт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "перебивать"
      }
    ]
  },
  {
    "id": 445,
    "english": "into",
    "transcription": "ˈɪntə",
    "ru": "интэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "в"
      }
    ]
  },
  {
    "id": 446,
    "english": "is",
    "transcription": "ɪz",
    "ru": "из",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "есть"
      }
    ]
  },
  {
    "id": 447,
    "english": "isn't",
    "transcription": "ˈɪznt",
    "ru": "изнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не есть"
      }
    ]
  },
  {
    "id": 448,
    "english": "it",
    "transcription": "ɪt",
    "ru": "ит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "оно"
      }
    ]
  },
  {
    "id": 449,
    "english": "it's",
    "transcription": "ɪts",
    "ru": "итс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "это есть"
      }
    ]
  },
  {
    "id": 450,
    "english": "its",
    "transcription": "ɪts",
    "ru": "итс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "его"
      }
    ]
  },
  {
    "id": 451,
    "english": "jacket",
    "transcription": "ˈdʒækɪt",
    "ru": "джэкит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "куртка"
      }
    ]
  },
  {
    "id": 452,
    "english": "jeans",
    "transcription": "dʒiːnz",
    "ru": "джинз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "джинсы"
      }
    ]
  },
  {
    "id": 453,
    "english": "jerk",
    "transcription": "dʒɜːk",
    "ru": "джёк",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "придурок"
      }
    ]
  },
  {
    "id": 454,
    "english": "job",
    "transcription": "dʒɒb",
    "ru": "джоб",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "работа"
      }
    ]
  },
  {
    "id": 455,
    "english": "join",
    "transcription": "dʒɔɪn",
    "ru": "джойн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "присоединиться"
      }
    ]
  },
  {
    "id": 456,
    "english": "joke",
    "transcription": "dʒəʊk",
    "ru": "джоук",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "шутка"
      }
    ]
  },
  {
    "id": 457,
    "english": "jump",
    "transcription": "dʒʌmp",
    "ru": "джамп",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "прыгать"
      }
    ]
  },
  {
    "id": 458,
    "english": "just",
    "transcription": "dʒʌst",
    "ru": "джаст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "просто"
      }
    ]
  },
  {
    "id": 459,
    "english": "keep",
    "transcription": "kiːp",
    "ru": "кип",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хранить"
      }
    ]
  },
  {
    "id": 460,
    "english": "kept",
    "transcription": "kept",
    "ru": "кэпт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "хранил"
      }
    ]
  },
  {
    "id": 461,
    "english": "key",
    "transcription": "kiː",
    "ru": "ки",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ключ"
      }
    ]
  },
  {
    "id": 462,
    "english": "kick",
    "transcription": "kɪk",
    "ru": "кик",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пинать"
      }
    ]
  },
  {
    "id": 463,
    "english": "kid",
    "transcription": "kɪd",
    "ru": "кид",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ребёнок"
      }
    ]
  },
  {
    "id": 464,
    "english": "kill",
    "transcription": "kɪl",
    "ru": "кил",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "убивать"
      }
    ]
  },
  {
    "id": 465,
    "english": "kind",
    "transcription": "kaɪnd",
    "ru": "кайнд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "добрый"
      }
    ]
  },
  {
    "id": 466,
    "english": "kiss",
    "transcription": "kɪs",
    "ru": "кис",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "целовать"
      }
    ]
  },
  {
    "id": 467,
    "english": "kitchen",
    "transcription": "ˈkɪtʃɪn",
    "ru": "китчин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кухня"
      }
    ]
  },
  {
    "id": 468,
    "english": "knee",
    "transcription": "niː",
    "ru": "ни",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "колено"
      }
    ]
  },
  {
    "id": 469,
    "english": "knew",
    "transcription": "njuː",
    "ru": "нью",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "знал"
      }
    ]
  },
  {
    "id": 470,
    "english": "knock",
    "transcription": "nɒk",
    "ru": "нок",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "стучать"
      }
    ]
  },
  {
    "id": 471,
    "english": "know",
    "transcription": "nəʊ",
    "ru": "ноу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "знать"
      }
    ]
  },
  {
    "id": 472,
    "english": "known",
    "transcription": "nəʊn",
    "ru": "ноун",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "известный"
      }
    ]
  },
  {
    "id": 473,
    "english": "lady",
    "transcription": "ˈleɪdi",
    "ru": "лэйди",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "леди"
      }
    ]
  },
  {
    "id": 474,
    "english": "land",
    "transcription": "lænd",
    "ru": "лэнд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "земля"
      }
    ]
  },
  {
    "id": 475,
    "english": "large",
    "transcription": "lɑːdʒ",
    "ru": "лардж",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "большой"
      }
    ]
  },
  {
    "id": 476,
    "english": "last",
    "transcription": "lɑːst",
    "ru": "ласт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "последний"
      }
    ]
  },
  {
    "id": 477,
    "english": "late",
    "transcription": "leɪt",
    "ru": "лэйт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "поздний"
      }
    ]
  },
  {
    "id": 478,
    "english": "laugh",
    "transcription": "lɑːf",
    "ru": "лаф",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "смеяться"
      }
    ]
  },
  {
    "id": 479,
    "english": "lay",
    "transcription": "leɪ",
    "ru": "лэй",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "класть"
      }
    ]
  },
  {
    "id": 480,
    "english": "lead",
    "transcription": "liːd",
    "ru": "лид",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вести"
      }
    ]
  },
  {
    "id": 481,
    "english": "lean",
    "transcription": "liːn",
    "ru": "лин",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "опираться"
      }
    ]
  },
  {
    "id": 482,
    "english": "learn",
    "transcription": "lɜːn",
    "ru": "лён",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "учить"
      }
    ]
  },
  {
    "id": 483,
    "english": "least",
    "transcription": "liːst",
    "ru": "лист",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "наименьший"
      }
    ]
  },
  {
    "id": 484,
    "english": "leave",
    "transcription": "liːv",
    "ru": "лив",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "покидать"
      }
    ]
  },
  {
    "id": 485,
    "english": "led",
    "transcription": "led",
    "ru": "лэд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вёл"
      }
    ]
  },
  {
    "id": 486,
    "english": "left",
    "transcription": "left",
    "ru": "лэфт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "левый"
      }
    ]
  },
  {
    "id": 487,
    "english": "leg",
    "transcription": "leɡ",
    "ru": "лэг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нога"
      }
    ]
  },
  {
    "id": 488,
    "english": "less",
    "transcription": "les",
    "ru": "лэс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "меньше"
      }
    ]
  },
  {
    "id": 489,
    "english": "let",
    "transcription": "let",
    "ru": "лэт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "позволять"
      }
    ]
  },
  {
    "id": 490,
    "english": "letter",
    "transcription": "ˈletə",
    "ru": "лэтэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "письмо"
      }
    ]
  },
  {
    "id": 491,
    "english": "lie",
    "transcription": "laɪ",
    "ru": "лай",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "лежать"
      }
    ]
  },
  {
    "id": 492,
    "english": "life",
    "transcription": "laɪf",
    "ru": "лайф",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "жизнь"
      }
    ]
  },
  {
    "id": 493,
    "english": "lift",
    "transcription": "lɪft",
    "ru": "лифт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "поднимать"
      }
    ]
  },
  {
    "id": 494,
    "english": "light",
    "transcription": "laɪt",
    "ru": "лайт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "свет"
      }
    ]
  },
  {
    "id": 495,
    "english": "like",
    "transcription": "laɪk",
    "ru": "лайк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нравиться"
      }
    ]
  },
  {
    "id": 496,
    "english": "line",
    "transcription": "laɪn",
    "ru": "лайн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "линия"
      }
    ]
  },
  {
    "id": 497,
    "english": "lip",
    "transcription": "lɪp",
    "ru": "лип",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "губа"
      }
    ]
  },
  {
    "id": 498,
    "english": "listen",
    "transcription": "ˈlɪsn",
    "ru": "лисн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "слушать"
      }
    ]
  },
  {
    "id": 499,
    "english": "little",
    "transcription": "ˈlɪtl",
    "ru": "литл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "маленький"
      }
    ]
  },
  {
    "id": 500,
    "english": "live",
    "transcription": "lɪv",
    "ru": "лив",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "жить"
      }
    ]
  },
  {
    "id": 501,
    "english": "lock",
    "transcription": "lɒk",
    "ru": "лок",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "замок"
      }
    ]
  },
  {
    "id": 502,
    "english": "locker",
    "transcription": "ˈlɒkə",
    "ru": "локэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "шкафчик"
      }
    ]
  },
  {
    "id": 503,
    "english": "long",
    "transcription": "lɒŋ",
    "ru": "лонг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "длинный"
      }
    ]
  },
  {
    "id": 504,
    "english": "look",
    "transcription": "lʊk",
    "ru": "лук",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "смотреть"
      }
    ]
  },
  {
    "id": 505,
    "english": "lose",
    "transcription": "luːz",
    "ru": "луз",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "терять"
      }
    ]
  },
  {
    "id": 506,
    "english": "lost",
    "transcription": "lɒst",
    "ru": "лост",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "потерянный"
      }
    ]
  },
  {
    "id": 507,
    "english": "lot",
    "transcription": "lɒt",
    "ru": "лот",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "много"
      }
    ]
  },
  {
    "id": 508,
    "english": "loud",
    "transcription": "laʊd",
    "ru": "лауд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "громкий"
      }
    ]
  },
  {
    "id": 509,
    "english": "love",
    "transcription": "lʌv",
    "ru": "лав",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "любовь"
      }
    ]
  },
  {
    "id": 510,
    "english": "low",
    "transcription": "ləʊ",
    "ru": "лоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "низкий"
      }
    ]
  },
  {
    "id": 511,
    "english": "lunch",
    "transcription": "lʌntʃ",
    "ru": "ланч",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "обед"
      }
    ]
  },
  {
    "id": 512,
    "english": "mad",
    "transcription": "mæd",
    "ru": "мэд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "злой"
      }
    ]
  },
  {
    "id": 513,
    "english": "made",
    "transcription": "meɪd",
    "ru": "мейд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сделал"
      }
    ]
  },
  {
    "id": 514,
    "english": "make",
    "transcription": "meɪk",
    "ru": "мейк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "делать"
      }
    ]
  },
  {
    "id": 515,
    "english": "man",
    "transcription": "mæn",
    "ru": "мэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мужчина"
      }
    ]
  },
  {
    "id": 516,
    "english": "manage",
    "transcription": "ˈmænɪdʒ",
    "ru": "мэнидж",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "управлять"
      }
    ]
  },
  {
    "id": 517,
    "english": "many",
    "transcription": "ˈmeni",
    "ru": "мени",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "много"
      }
    ]
  },
  {
    "id": 518,
    "english": "mark",
    "transcription": "mɑːk",
    "ru": "марк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "отметка"
      }
    ]
  },
  {
    "id": 519,
    "english": "marry",
    "transcription": "ˈmæri",
    "ru": "мэри",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "жениться"
      }
    ]
  },
  {
    "id": 520,
    "english": "match",
    "transcription": "mætʃ",
    "ru": "мэтч",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "матч"
      }
    ]
  },
  {
    "id": 521,
    "english": "matter",
    "transcription": "ˈmætə",
    "ru": "мэтэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "дело"
      }
    ]
  },
  {
    "id": 522,
    "english": "may",
    "transcription": "meɪ",
    "ru": "мей",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мочь"
      }
    ]
  },
  {
    "id": 523,
    "english": "maybe",
    "transcription": "ˈmeɪbi",
    "ru": "мейби",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "может быть"
      }
    ]
  },
  {
    "id": 524,
    "english": "me",
    "transcription": "miː",
    "ru": "ми",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мне"
      }
    ]
  },
  {
    "id": 525,
    "english": "mean",
    "transcription": "miːn",
    "ru": "мин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "значить"
      }
    ]
  },
  {
    "id": 526,
    "english": "meant",
    "transcription": "ment",
    "ru": "мент",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "имел в виду"
      }
    ]
  },
  {
    "id": 527,
    "english": "meet",
    "transcription": "miːt",
    "ru": "мит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "встречать"
      }
    ]
  },
  {
    "id": 528,
    "english": "memory",
    "transcription": "ˈmeməri",
    "ru": "мемэри",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "память"
      }
    ]
  },
  {
    "id": 529,
    "english": "men",
    "transcription": "men",
    "ru": "мен",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мужчины"
      }
    ]
  },
  {
    "id": 530,
    "english": "mention",
    "transcription": "ˈmenʃən",
    "ru": "меншн",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "упоминать"
      }
    ]
  },
  {
    "id": 531,
    "english": "met",
    "transcription": "met",
    "ru": "мет",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "встретил"
      }
    ]
  },
  {
    "id": 532,
    "english": "middle",
    "transcription": "ˈmɪdl",
    "ru": "мидл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "середина"
      }
    ]
  },
  {
    "id": 533,
    "english": "might",
    "transcription": "maɪt",
    "ru": "майт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мог бы"
      }
    ]
  },
  {
    "id": 534,
    "english": "mind",
    "transcription": "maɪnd",
    "ru": "майнд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "разум"
      }
    ]
  },
  {
    "id": 535,
    "english": "mine",
    "transcription": "maɪn",
    "ru": "майн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мой"
      }
    ]
  },
  {
    "id": 536,
    "english": "minute",
    "transcription": "ˈmɪnɪt",
    "ru": "минит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "минута"
      }
    ]
  },
  {
    "id": 537,
    "english": "mirror",
    "transcription": "ˈmɪrə",
    "ru": "мирэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "зеркало"
      }
    ]
  },
  {
    "id": 538,
    "english": "miss",
    "transcription": "mɪs",
    "ru": "мис",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "скучать"
      }
    ]
  },
  {
    "id": 539,
    "english": "mom",
    "transcription": "mɒm",
    "ru": "мом",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мама"
      }
    ]
  },
  {
    "id": 540,
    "english": "moment",
    "transcription": "ˈməʊmənt",
    "ru": "моумэнт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "момент"
      }
    ]
  },
  {
    "id": 541,
    "english": "money",
    "transcription": "ˈmʌni",
    "ru": "мани",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "деньги"
      }
    ]
  },
  {
    "id": 542,
    "english": "month",
    "transcription": "mʌnθ",
    "ru": "манс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "месяц"
      }
    ]
  },
  {
    "id": 543,
    "english": "mood",
    "transcription": "muːd",
    "ru": "муд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "настроение"
      }
    ]
  },
  {
    "id": 544,
    "english": "more",
    "transcription": "mɔː",
    "ru": "мор",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "больше"
      }
    ]
  },
  {
    "id": 545,
    "english": "morning",
    "transcription": "ˈmɔːnɪŋ",
    "ru": "морнинг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "утро"
      }
    ]
  },
  {
    "id": 546,
    "english": "most",
    "transcription": "məʊst",
    "ru": "моуст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "большинство"
      }
    ]
  },
  {
    "id": 547,
    "english": "mother",
    "transcription": "ˈmʌðə",
    "ru": "мазэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мать"
      }
    ]
  },
  {
    "id": 548,
    "english": "mouth",
    "transcription": "maʊθ",
    "ru": "маус",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рот"
      }
    ]
  },
  {
    "id": 549,
    "english": "move",
    "transcription": "muːv",
    "ru": "мув",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "двигаться"
      }
    ]
  },
  {
    "id": 550,
    "english": "movie",
    "transcription": "ˈmuːvi",
    "ru": "муви",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "фильм"
      }
    ]
  },
  {
    "id": 551,
    "english": "mr.",
    "transcription": "ˈmɪstə",
    "ru": "мистэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "господин"
      }
    ]
  },
  {
    "id": 552,
    "english": "mrs.",
    "transcription": "ˈmɪsɪz",
    "ru": "мисиз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "госпожа"
      }
    ]
  },
  {
    "id": 553,
    "english": "much",
    "transcription": "mʌtʃ",
    "ru": "мач",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "много"
      }
    ]
  },
  {
    "id": 554,
    "english": "mum",
    "transcription": "mʌm",
    "ru": "мам",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мама"
      }
    ]
  },
  {
    "id": 555,
    "english": "mumble",
    "transcription": "ˈmʌmbl",
    "ru": "мамбл",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бормотать"
      }
    ]
  },
  {
    "id": 556,
    "english": "music",
    "transcription": "ˈmjuːzɪk",
    "ru": "мьюзик",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "музыка"
      }
    ]
  },
  {
    "id": 557,
    "english": "must",
    "transcription": "mʌst",
    "ru": "маст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "должен"
      }
    ]
  },
  {
    "id": 558,
    "english": "mutter",
    "transcription": "ˈmʌtə",
    "ru": "матэ",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бормотать"
      }
    ]
  },
  {
    "id": 559,
    "english": "my",
    "transcription": "maɪ",
    "ru": "май",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мой"
      }
    ]
  },
  {
    "id": 560,
    "english": "myself",
    "transcription": "maɪˈself",
    "ru": "майсэлф",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "себя"
      }
    ]
  },
  {
    "id": 561,
    "english": "name",
    "transcription": "neɪm",
    "ru": "нейм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "имя"
      }
    ]
  },
  {
    "id": 562,
    "english": "near",
    "transcription": "nɪə",
    "ru": "ниэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "близко"
      }
    ]
  },
  {
    "id": 563,
    "english": "nearly",
    "transcription": "ˈnɪəli",
    "ru": "ниэли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "почти"
      }
    ]
  },
  {
    "id": 564,
    "english": "neck",
    "transcription": "nek",
    "ru": "нек",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "шея"
      }
    ]
  },
  {
    "id": 565,
    "english": "need",
    "transcription": "niːd",
    "ru": "нид",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нуждаться"
      }
    ]
  },
  {
    "id": 566,
    "english": "nervous",
    "transcription": "ˈnɜːvəs",
    "ru": "нёрвэс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нервный"
      }
    ]
  },
  {
    "id": 567,
    "english": "never",
    "transcription": "ˈnevə",
    "ru": "невэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "никогда"
      }
    ]
  },
  {
    "id": 568,
    "english": "new",
    "transcription": "njuː",
    "ru": "нью",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "новый"
      }
    ]
  },
  {
    "id": 569,
    "english": "next",
    "transcription": "nekst",
    "ru": "некст",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "следующий"
      }
    ]
  },
  {
    "id": 570,
    "english": "nice",
    "transcription": "naɪs",
    "ru": "найс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хороший"
      }
    ]
  },
  {
    "id": 571,
    "english": "night",
    "transcription": "naɪt",
    "ru": "найт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ночь"
      }
    ]
  },
  {
    "id": 572,
    "english": "no",
    "transcription": "nəʊ",
    "ru": "ноу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нет"
      }
    ]
  },
  {
    "id": 573,
    "english": "nod",
    "transcription": "nɒd",
    "ru": "нод",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кивать"
      }
    ]
  },
  {
    "id": 574,
    "english": "noise",
    "transcription": "nɔɪz",
    "ru": "нойз",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "шум"
      }
    ]
  },
  {
    "id": 575,
    "english": "none",
    "transcription": "nʌn",
    "ru": "нан",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ни один"
      }
    ]
  },
  {
    "id": 576,
    "english": "normal",
    "transcription": "ˈnɔːml",
    "ru": "нормл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "нормальный"
      }
    ]
  },
  {
    "id": 577,
    "english": "nose",
    "transcription": "nəʊz",
    "ru": "ноуз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нос"
      }
    ]
  },
  {
    "id": 578,
    "english": "not",
    "transcription": "nɒt",
    "ru": "нот",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не"
      }
    ]
  },
  {
    "id": 579,
    "english": "note",
    "transcription": "nəʊt",
    "ru": "ноут",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "заметка"
      }
    ]
  },
  {
    "id": 580,
    "english": "nothing",
    "transcription": "ˈnʌθɪŋ",
    "ru": "насинг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ничего"
      }
    ]
  },
  {
    "id": 581,
    "english": "notice",
    "transcription": "ˈnəʊtɪs",
    "ru": "ноутис",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "замечать"
      }
    ]
  },
  {
    "id": 582,
    "english": "now",
    "transcription": "naʊ",
    "ru": "нау",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сейчас"
      }
    ]
  },
  {
    "id": 583,
    "english": "number",
    "transcription": "ˈnʌmbə",
    "ru": "намбэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "число"
      }
    ]
  },
  {
    "id": 584,
    "english": "obviously",
    "transcription": "ˈɒbviəsli",
    "ru": "обвиэсли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "очевидно"
      }
    ]
  },
  {
    "id": 585,
    "english": "of",
    "transcription": "ɒv",
    "ru": "ов",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "из"
      }
    ]
  },
  {
    "id": 586,
    "english": "off",
    "transcription": "ɒf",
    "ru": "оф",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "выкл"
      }
    ]
  },
  {
    "id": 587,
    "english": "offer",
    "transcription": "ˈɒfə",
    "ru": "офэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "предлагать"
      }
    ]
  },
  {
    "id": 588,
    "english": "office",
    "transcription": "ˈɒfɪs",
    "ru": "офис",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "офис"
      }
    ]
  },
  {
    "id": 589,
    "english": "often",
    "transcription": "ˈɒfn",
    "ru": "офн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "часто"
      }
    ]
  },
  {
    "id": 590,
    "english": "oh",
    "transcription": "əʊ",
    "ru": "оу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "о"
      }
    ]
  },
  {
    "id": 591,
    "english": "okay",
    "transcription": "ˌəʊˈkeɪ",
    "ru": "окей",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хорошо"
      }
    ]
  },
  {
    "id": 592,
    "english": "old",
    "transcription": "əʊld",
    "ru": "оулд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "старый"
      }
    ]
  },
  {
    "id": 593,
    "english": "on",
    "transcription": "ɒn",
    "ru": "он",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "на"
      }
    ]
  },
  {
    "id": 594,
    "english": "once",
    "transcription": "wʌns",
    "ru": "уанс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "однажды"
      }
    ]
  },
  {
    "id": 595,
    "english": "one",
    "transcription": "wʌn",
    "ru": "уан",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "один"
      }
    ]
  },
  {
    "id": 596,
    "english": "only",
    "transcription": "ˈəʊnli",
    "ru": "оунли",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "только"
      }
    ]
  },
  {
    "id": 597,
    "english": "onto",
    "transcription": "ˈɒntə",
    "ru": "онтэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "на"
      }
    ]
  },
  {
    "id": 598,
    "english": "open",
    "transcription": "ˈəʊpən",
    "ru": "оупэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "открывать"
      }
    ]
  },
  {
    "id": 599,
    "english": "or",
    "transcription": "ɔː",
    "ru": "ор",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "или"
      }
    ]
  },
  {
    "id": 600,
    "english": "order",
    "transcription": "ˈɔːdə",
    "ru": "ордэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "порядок"
      }
    ]
  },
  {
    "id": 601,
    "english": "other",
    "transcription": "ˈʌðə",
    "ru": "азэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "другой"
      }
    ]
  },
  {
    "id": 602,
    "english": "our",
    "transcription": "ˈaʊə",
    "ru": "ауэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "наш"
      }
    ]
  },
  {
    "id": 603,
    "english": "out",
    "transcription": "aʊt",
    "ru": "аут",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "наружу"
      }
    ]
  },
  {
    "id": 604,
    "english": "outside",
    "transcription": "ˌaʊtˈsaɪd",
    "ru": "аутсайд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "снаружи"
      }
    ]
  },
  {
    "id": 605,
    "english": "over",
    "transcription": "ˈəʊvə",
    "ru": "оувэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "над"
      }
    ]
  },
  {
    "id": 606,
    "english": "own",
    "transcription": "əʊn",
    "ru": "оун",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "собственный"
      }
    ]
  },
  {
    "id": 607,
    "english": "pack",
    "transcription": "pæk",
    "ru": "пэк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пакет"
      }
    ]
  },
  {
    "id": 608,
    "english": "pain",
    "transcription": "peɪn",
    "ru": "пэйн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "боль"
      }
    ]
  },
  {
    "id": 609,
    "english": "paint",
    "transcription": "peɪnt",
    "ru": "пэйнт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "краска"
      }
    ]
  },
  {
    "id": 610,
    "english": "pair",
    "transcription": "peə",
    "ru": "пэа",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пара"
      }
    ]
  },
  {
    "id": 611,
    "english": "pants",
    "transcription": "pænts",
    "ru": "пэнтс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "брюки"
      }
    ]
  },
  {
    "id": 612,
    "english": "paper",
    "transcription": "ˈpeɪpə",
    "ru": "пэйпэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "бумага"
      }
    ]
  },
  {
    "id": 613,
    "english": "parents",
    "transcription": "ˈpeərənts",
    "ru": "пэарэнтс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "родители"
      }
    ]
  },
  {
    "id": 614,
    "english": "park",
    "transcription": "pɑːk",
    "ru": "паак",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "парк"
      }
    ]
  },
  {
    "id": 615,
    "english": "part",
    "transcription": "pɑːt",
    "ru": "паат",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "часть"
      }
    ]
  },
  {
    "id": 616,
    "english": "party",
    "transcription": "ˈpɑːti",
    "ru": "паати",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вечеринка"
      }
    ]
  },
  {
    "id": 617,
    "english": "pass",
    "transcription": "pɑːs",
    "ru": "паас",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "проходить"
      }
    ]
  },
  {
    "id": 618,
    "english": "past",
    "transcription": "pɑːst",
    "ru": "пааст",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "прошлое"
      }
    ]
  },
  {
    "id": 619,
    "english": "pause",
    "transcription": "pɔːz",
    "ru": "пооз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пауза"
      }
    ]
  },
  {
    "id": 620,
    "english": "pay",
    "transcription": "peɪ",
    "ru": "пэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "платить"
      }
    ]
  },
  {
    "id": 621,
    "english": "people",
    "transcription": "ˈpiːpl",
    "ru": "пиипл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "люди"
      }
    ]
  },
  {
    "id": 622,
    "english": "perfect",
    "transcription": "ˈpɜːfɪkt",
    "ru": "пёфикт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "идеальный"
      }
    ]
  },
  {
    "id": 623,
    "english": "perhaps",
    "transcription": "pəˈhæps",
    "ru": "пэхэпс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "возможно"
      }
    ]
  },
  {
    "id": 624,
    "english": "person",
    "transcription": "ˈpɜːsn",
    "ru": "пёсн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "человек"
      }
    ]
  },
  {
    "id": 625,
    "english": "phone",
    "transcription": "fəʊn",
    "ru": "фоун",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "телефон"
      }
    ]
  },
  {
    "id": 626,
    "english": "pick",
    "transcription": "pɪk",
    "ru": "пик",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "выбирать"
      }
    ]
  },
  {
    "id": 627,
    "english": "picture",
    "transcription": "ˈpɪktʃə",
    "ru": "пикчэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "картинка"
      }
    ]
  },
  {
    "id": 628,
    "english": "piece",
    "transcription": "piːs",
    "ru": "пиис",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кусок"
      }
    ]
  },
  {
    "id": 629,
    "english": "pink",
    "transcription": "pɪŋk",
    "ru": "пинк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "розовый"
      }
    ]
  },
  {
    "id": 630,
    "english": "piss",
    "transcription": "pɪs",
    "ru": "пис",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мочиться"
      }
    ]
  },
  {
    "id": 631,
    "english": "place",
    "transcription": "pleɪs",
    "ru": "плэйс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "место"
      }
    ]
  },
  {
    "id": 632,
    "english": "plan",
    "transcription": "plæn",
    "ru": "плэн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "план"
      }
    ]
  },
  {
    "id": 633,
    "english": "play",
    "transcription": "pleɪ",
    "ru": "плэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "играть"
      }
    ]
  },
  {
    "id": 634,
    "english": "please",
    "transcription": "pliːz",
    "ru": "плииз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пожалуйста"
      }
    ]
  },
  {
    "id": 635,
    "english": "pocket",
    "transcription": "ˈpɒkɪt",
    "ru": "покит",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "карман"
      }
    ]
  },
  {
    "id": 636,
    "english": "point",
    "transcription": "pɔɪnt",
    "ru": "поинт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "точка"
      }
    ]
  },
  {
    "id": 637,
    "english": "police",
    "transcription": "pəˈliːs",
    "ru": "пэлиис",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "полиция"
      }
    ]
  },
  {
    "id": 638,
    "english": "pop",
    "transcription": "pɒp",
    "ru": "поп",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хлопать"
      }
    ]
  },
  {
    "id": 639,
    "english": "position",
    "transcription": "pəˈzɪʃn",
    "ru": "пэзишн",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "позиция"
      }
    ]
  },
  {
    "id": 640,
    "english": "possible",
    "transcription": "ˈpɒsəbl",
    "ru": "посэбл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "возможный"
      }
    ]
  },
  {
    "id": 641,
    "english": "power",
    "transcription": "ˈpaʊə",
    "ru": "пауэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сила"
      }
    ]
  },
  {
    "id": 642,
    "english": "practically",
    "transcription": "ˈpræktɪkli",
    "ru": "прэктикли",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "практически"
      }
    ]
  },
  {
    "id": 643,
    "english": "present",
    "transcription": "ˈpreznt",
    "ru": "презнт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "подарок"
      }
    ]
  },
  {
    "id": 644,
    "english": "press",
    "transcription": "pres",
    "ru": "прес",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "нажимать"
      }
    ]
  },
  {
    "id": 645,
    "english": "pretend",
    "transcription": "prɪˈtend",
    "ru": "притенд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "притворяться"
      }
    ]
  },
  {
    "id": 646,
    "english": "pretty",
    "transcription": "ˈprɪti",
    "ru": "прити",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "красивый"
      }
    ]
  },
  {
    "id": 647,
    "english": "probably",
    "transcription": "ˈprɒbəbli",
    "ru": "пробэбли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вероятно"
      }
    ]
  },
  {
    "id": 648,
    "english": "problem",
    "transcription": "ˈprɒbləm",
    "ru": "проблэм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "проблема"
      }
    ]
  },
  {
    "id": 649,
    "english": "promise",
    "transcription": "ˈprɒmɪs",
    "ru": "промис",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "обещать"
      }
    ]
  },
  {
    "id": 650,
    "english": "pull",
    "transcription": "pʊl",
    "ru": "пул",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "тянуть"
      }
    ]
  },
  {
    "id": 651,
    "english": "punch",
    "transcription": "pʌntʃ",
    "ru": "панч",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "удар"
      }
    ]
  },
  {
    "id": 652,
    "english": "push",
    "transcription": "pʊʃ",
    "ru": "пуш",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "толкать"
      }
    ]
  },
  {
    "id": 653,
    "english": "put",
    "transcription": "pʊt",
    "ru": "пут",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "класть"
      }
    ]
  },
  {
    "id": 654,
    "english": "question",
    "transcription": "ˈkwestʃən",
    "ru": "куэсчэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вопрос"
      }
    ]
  },
  {
    "id": 655,
    "english": "quick",
    "transcription": "kwɪk",
    "ru": "куик",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "быстрый"
      }
    ]
  },
  {
    "id": 656,
    "english": "quickly",
    "transcription": "ˈkwɪkli",
    "ru": "куикли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "быстро"
      }
    ]
  },
  {
    "id": 657,
    "english": "quiet",
    "transcription": "ˈkwaɪət",
    "ru": "куайэт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "тихий"
      }
    ]
  },
  {
    "id": 658,
    "english": "quietly",
    "transcription": "ˈkwaɪətli",
    "ru": "куайэтли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тихо"
      }
    ]
  },
  {
    "id": 659,
    "english": "quite",
    "transcription": "kwaɪt",
    "ru": "куайт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "довольно"
      }
    ]
  },
  {
    "id": 660,
    "english": "race",
    "transcription": "reɪs",
    "ru": "рэйс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "гонка"
      }
    ]
  },
  {
    "id": 661,
    "english": "rain",
    "transcription": "reɪn",
    "ru": "рэйн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дождь"
      }
    ]
  },
  {
    "id": 662,
    "english": "raise",
    "transcription": "reɪz",
    "ru": "рэйз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "поднимать"
      }
    ]
  },
  {
    "id": 663,
    "english": "ran",
    "transcription": "ræn",
    "ru": "рэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "бежал"
      }
    ]
  },
  {
    "id": 664,
    "english": "rang",
    "transcription": "ræŋ",
    "ru": "рэн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "звонил"
      }
    ]
  },
  {
    "id": 665,
    "english": "rather",
    "transcription": "ˈrɑːðə",
    "ru": "рааза",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "скорее"
      }
    ]
  },
  {
    "id": 666,
    "english": "reach",
    "transcription": "riːtʃ",
    "ru": "риич",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "достигать"
      }
    ]
  },
  {
    "id": 667,
    "english": "read",
    "transcription": "riːd",
    "ru": "риид",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "читать"
      }
    ]
  },
  {
    "id": 668,
    "english": "ready",
    "transcription": "ˈredi",
    "ru": "реди",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "готовый"
      }
    ]
  },
  {
    "id": 669,
    "english": "real",
    "transcription": "rɪəl",
    "ru": "риэл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "настоящий"
      }
    ]
  },
  {
    "id": 670,
    "english": "realize",
    "transcription": "ˈrɪəlaɪz",
    "ru": "риэлайз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "осознавать"
      }
    ]
  },
  {
    "id": 671,
    "english": "really",
    "transcription": "ˈrɪəli",
    "ru": "риэли",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "действительно"
      }
    ]
  },
  {
    "id": 672,
    "english": "reason",
    "transcription": "ˈriːzn",
    "ru": "риизн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "причина"
      }
    ]
  },
  {
    "id": 673,
    "english": "recognize",
    "transcription": "ˈrekəɡnaɪz",
    "ru": "рекэгнайз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "узнавать"
      }
    ]
  },
  {
    "id": 674,
    "english": "red",
    "transcription": "red",
    "ru": "ред",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "красный"
      }
    ]
  },
  {
    "id": 675,
    "english": "relationship",
    "transcription": "rɪˈleɪʃnʃɪp",
    "ru": "рилэйшншип",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "отношения"
      }
    ]
  },
  {
    "id": 676,
    "english": "relax",
    "transcription": "rɪˈlæks",
    "ru": "рилэкс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "расслабляться"
      }
    ]
  },
  {
    "id": 677,
    "english": "remain",
    "transcription": "rɪˈmeɪn",
    "ru": "римэйн",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "оставаться"
      }
    ]
  },
  {
    "id": 678,
    "english": "remember",
    "transcription": "rɪˈmembə",
    "ru": "римембэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "помнить"
      }
    ]
  },
  {
    "id": 679,
    "english": "remind",
    "transcription": "rɪˈmaɪnd",
    "ru": "римайнд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "напоминать"
      }
    ]
  },
  {
    "id": 680,
    "english": "repeat",
    "transcription": "rɪˈpiːt",
    "ru": "рипиит",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "повторять"
      }
    ]
  },
  {
    "id": 681,
    "english": "reply",
    "transcription": "rɪˈplaɪ",
    "ru": "риплай",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "отвечать"
      }
    ]
  },
  {
    "id": 682,
    "english": "respond",
    "transcription": "rɪˈspɒnd",
    "ru": "риспонд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "реагировать"
      }
    ]
  },
  {
    "id": 683,
    "english": "rest",
    "transcription": "rest",
    "ru": "рест",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "отдых"
      }
    ]
  },
  {
    "id": 684,
    "english": "return",
    "transcription": "rɪˈtɜːn",
    "ru": "ритён",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "возвращаться"
      }
    ]
  },
  {
    "id": 685,
    "english": "ride",
    "transcription": "raɪd",
    "ru": "райд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ездить"
      }
    ]
  },
  {
    "id": 686,
    "english": "right",
    "transcription": "raɪt",
    "ru": "райт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "правильный"
      }
    ]
  },
  {
    "id": 687,
    "english": "ring",
    "transcription": "rɪŋ",
    "ru": "ринг",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кольцо"
      }
    ]
  },
  {
    "id": 688,
    "english": "road",
    "transcription": "rəʊd",
    "ru": "роуд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дорога"
      }
    ]
  },
  {
    "id": 689,
    "english": "rock",
    "transcription": "rɒk",
    "ru": "рок",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "камень"
      }
    ]
  },
  {
    "id": 690,
    "english": "roll",
    "transcription": "rəʊl",
    "ru": "роул",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "катить"
      }
    ]
  },
  {
    "id": 691,
    "english": "room",
    "transcription": "ruːm",
    "ru": "руум",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "комната"
      }
    ]
  },
  {
    "id": 692,
    "english": "rose",
    "transcription": "rəʊz",
    "ru": "роуз",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "роза"
      }
    ]
  },
  {
    "id": 693,
    "english": "round",
    "transcription": "raʊnd",
    "ru": "раунд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "круглый"
      }
    ]
  },
  {
    "id": 694,
    "english": "rub",
    "transcription": "rʌb",
    "ru": "раб",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тереть"
      }
    ]
  },
  {
    "id": 695,
    "english": "run",
    "transcription": "rʌn",
    "ru": "ран",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "бежать"
      }
    ]
  },
  {
    "id": 696,
    "english": "rush",
    "transcription": "rʌʃ",
    "ru": "раш",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "спешить"
      }
    ]
  },
  {
    "id": 697,
    "english": "sad",
    "transcription": "sæd",
    "ru": "сэд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "грустный"
      }
    ]
  },
  {
    "id": 698,
    "english": "safe",
    "transcription": "seɪf",
    "ru": "сэйф",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "безопасный"
      }
    ]
  },
  {
    "id": 699,
    "english": "said",
    "transcription": "sed",
    "ru": "сед",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сказал"
      }
    ]
  },
  {
    "id": 700,
    "english": "same",
    "transcription": "seɪm",
    "ru": "сэйм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "одинаковый"
      }
    ]
  },
  {
    "id": 701,
    "english": "sat",
    "transcription": "sæt",
    "ru": "сэт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сидел"
      }
    ]
  },
  {
    "id": 702,
    "english": "save",
    "transcription": "seɪv",
    "ru": "сейв",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "спасать"
      }
    ]
  },
  {
    "id": 703,
    "english": "saw",
    "transcription": "sɔː",
    "ru": "со",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "видел"
      }
    ]
  },
  {
    "id": 704,
    "english": "say",
    "transcription": "seɪ",
    "ru": "сей",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сказать"
      }
    ]
  },
  {
    "id": 705,
    "english": "scare",
    "transcription": "skeə",
    "ru": "скэа",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пугать"
      }
    ]
  },
  {
    "id": 706,
    "english": "school",
    "transcription": "skuːl",
    "ru": "скул",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "школа"
      }
    ]
  },
  {
    "id": 707,
    "english": "scream",
    "transcription": "skriːm",
    "ru": "скрим",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кричать"
      }
    ]
  },
  {
    "id": 708,
    "english": "search",
    "transcription": "sɜːtʃ",
    "ru": "сёрч",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "поиск"
      }
    ]
  },
  {
    "id": 709,
    "english": "seat",
    "transcription": "siːt",
    "ru": "сит",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сиденье"
      }
    ]
  },
  {
    "id": 710,
    "english": "second",
    "transcription": "ˈsekənd",
    "ru": "сэконд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "второй"
      }
    ]
  },
  {
    "id": 711,
    "english": "see",
    "transcription": "siː",
    "ru": "си",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "видеть"
      }
    ]
  },
  {
    "id": 712,
    "english": "seem",
    "transcription": "siːm",
    "ru": "сим",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "казаться"
      }
    ]
  },
  {
    "id": 713,
    "english": "seen",
    "transcription": "siːn",
    "ru": "син",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "увиденный"
      }
    ]
  },
  {
    "id": 714,
    "english": "self",
    "transcription": "self",
    "ru": "сэлф",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сам"
      }
    ]
  },
  {
    "id": 715,
    "english": "send",
    "transcription": "send",
    "ru": "сэнд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "отправлять"
      }
    ]
  },
  {
    "id": 716,
    "english": "sense",
    "transcription": "sens",
    "ru": "сэнс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "смысл"
      }
    ]
  },
  {
    "id": 717,
    "english": "sent",
    "transcription": "sent",
    "ru": "сэнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "отправил"
      }
    ]
  },
  {
    "id": 718,
    "english": "serious",
    "transcription": "ˈsɪəriəs",
    "ru": "сириэс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "серьёзный"
      }
    ]
  },
  {
    "id": 719,
    "english": "seriously",
    "transcription": "ˈsɪəriəsli",
    "ru": "сириэсли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "серьёзно"
      }
    ]
  },
  {
    "id": 720,
    "english": "set",
    "transcription": "set",
    "ru": "сэт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "набор"
      }
    ]
  },
  {
    "id": 721,
    "english": "settle",
    "transcription": "ˈsetl",
    "ru": "сэтл",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "улаживать"
      }
    ]
  },
  {
    "id": 722,
    "english": "seven",
    "transcription": "ˈsevn",
    "ru": "сэвн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "семь"
      }
    ]
  },
  {
    "id": 723,
    "english": "several",
    "transcription": "ˈsevrəl",
    "ru": "сэврэл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "несколько"
      }
    ]
  },
  {
    "id": 724,
    "english": "shadow",
    "transcription": "ˈʃædəʊ",
    "ru": "шэдоу",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тень"
      }
    ]
  },
  {
    "id": 725,
    "english": "shake",
    "transcription": "ʃeɪk",
    "ru": "шейк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "трясти"
      }
    ]
  },
  {
    "id": 726,
    "english": "share",
    "transcription": "ʃeə",
    "ru": "шэа",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "делиться"
      }
    ]
  },
  {
    "id": 727,
    "english": "she",
    "transcription": "ʃiː",
    "ru": "ши",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "она"
      }
    ]
  },
  {
    "id": 728,
    "english": "she'd",
    "transcription": "ʃiːd",
    "ru": "шид",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "она бы"
      }
    ]
  },
  {
    "id": 729,
    "english": "she's",
    "transcription": "ʃiːz",
    "ru": "шиз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "она есть"
      }
    ]
  },
  {
    "id": 730,
    "english": "shift",
    "transcription": "ʃɪft",
    "ru": "шифт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сдвиг"
      }
    ]
  },
  {
    "id": 731,
    "english": "shirt",
    "transcription": "ʃɜːt",
    "ru": "шёт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рубашка"
      }
    ]
  },
  {
    "id": 732,
    "english": "shit",
    "transcription": "ʃɪt",
    "ru": "шит",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дерьмо"
      }
    ]
  },
  {
    "id": 733,
    "english": "shock",
    "transcription": "ʃɒk",
    "ru": "шок",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "шок"
      }
    ]
  },
  {
    "id": 734,
    "english": "shoe",
    "transcription": "ʃuː",
    "ru": "шу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ботинок"
      }
    ]
  },
  {
    "id": 735,
    "english": "shook",
    "transcription": "ʃʊk",
    "ru": "шук",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "тряс"
      }
    ]
  },
  {
    "id": 736,
    "english": "shop",
    "transcription": "ʃɒp",
    "ru": "шоп",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "магазин"
      }
    ]
  },
  {
    "id": 737,
    "english": "short",
    "transcription": "ʃɔːt",
    "ru": "шот",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "короткий"
      }
    ]
  },
  {
    "id": 738,
    "english": "shot",
    "transcription": "ʃɒt",
    "ru": "шот",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "выстрел"
      }
    ]
  },
  {
    "id": 739,
    "english": "should",
    "transcription": "ʃʊd",
    "ru": "шуд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "следует"
      }
    ]
  },
  {
    "id": 740,
    "english": "shoulder",
    "transcription": "ˈʃəʊldə",
    "ru": "шоулдэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "плечо"
      }
    ]
  },
  {
    "id": 741,
    "english": "shouldn't",
    "transcription": "ˈʃʊdnt",
    "ru": "шуднт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "не следует"
      }
    ]
  },
  {
    "id": 742,
    "english": "shout",
    "transcription": "ʃaʊt",
    "ru": "шаут",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кричать"
      }
    ]
  },
  {
    "id": 743,
    "english": "shove",
    "transcription": "ʃʌv",
    "ru": "шав",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "толкать"
      }
    ]
  },
  {
    "id": 744,
    "english": "show",
    "transcription": "ʃəʊ",
    "ru": "шоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "показывать"
      }
    ]
  },
  {
    "id": 745,
    "english": "shower",
    "transcription": "ˈʃaʊə",
    "ru": "шауэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "душ"
      }
    ]
  },
  {
    "id": 746,
    "english": "shrug",
    "transcription": "ʃrʌɡ",
    "ru": "шраг",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пожимать плечами"
      }
    ]
  },
  {
    "id": 747,
    "english": "shut",
    "transcription": "ʃʌt",
    "ru": "шат",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "закрывать"
      }
    ]
  },
  {
    "id": 748,
    "english": "sick",
    "transcription": "sɪk",
    "ru": "сик",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "больной"
      }
    ]
  },
  {
    "id": 749,
    "english": "side",
    "transcription": "saɪd",
    "ru": "сайд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сторона"
      }
    ]
  },
  {
    "id": 750,
    "english": "sigh",
    "transcription": "saɪ",
    "ru": "сай",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вздыхать"
      }
    ]
  },
  {
    "id": 751,
    "english": "sight",
    "transcription": "saɪt",
    "ru": "сайт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вид"
      }
    ]
  },
  {
    "id": 752,
    "english": "sign",
    "transcription": "saɪn",
    "ru": "сайн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "знак"
      }
    ]
  },
  {
    "id": 753,
    "english": "silence",
    "transcription": "ˈsaɪləns",
    "ru": "сайлэнс",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тишина"
      }
    ]
  },
  {
    "id": 754,
    "english": "silent",
    "transcription": "ˈsaɪlənt",
    "ru": "сайлэнт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тихий"
      }
    ]
  },
  {
    "id": 755,
    "english": "simply",
    "transcription": "ˈsɪmpli",
    "ru": "симпли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "просто"
      }
    ]
  },
  {
    "id": 756,
    "english": "since",
    "transcription": "sɪns",
    "ru": "синс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "с тех пор"
      }
    ]
  },
  {
    "id": 757,
    "english": "single",
    "transcription": "ˈsɪŋɡl",
    "ru": "сингл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "единственный"
      }
    ]
  },
  {
    "id": 758,
    "english": "sir",
    "transcription": "sɜː",
    "ru": "сёр",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сэр"
      }
    ]
  },
  {
    "id": 759,
    "english": "sister",
    "transcription": "ˈsɪstə",
    "ru": "систэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сестра"
      }
    ]
  },
  {
    "id": 760,
    "english": "sit",
    "transcription": "sɪt",
    "ru": "сит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сидеть"
      }
    ]
  },
  {
    "id": 761,
    "english": "situation",
    "transcription": "ˌsɪtʃuˈeɪʃn",
    "ru": "ситуэйшн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ситуация"
      }
    ]
  },
  {
    "id": 762,
    "english": "six",
    "transcription": "sɪks",
    "ru": "сикс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "шесть"
      }
    ]
  },
  {
    "id": 763,
    "english": "skin",
    "transcription": "skɪn",
    "ru": "скин",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "кожа"
      }
    ]
  },
  {
    "id": 764,
    "english": "sky",
    "transcription": "skaɪ",
    "ru": "скай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "небо"
      }
    ]
  },
  {
    "id": 765,
    "english": "slam",
    "transcription": "slæm",
    "ru": "слэм",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "хлопать"
      }
    ]
  },
  {
    "id": 766,
    "english": "sleep",
    "transcription": "sliːp",
    "ru": "слип",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "спать"
      }
    ]
  },
  {
    "id": 767,
    "english": "slightly",
    "transcription": "ˈslaɪtli",
    "ru": "слайтли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "слегка"
      }
    ]
  },
  {
    "id": 768,
    "english": "slip",
    "transcription": "slɪp",
    "ru": "слип",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "скользить"
      }
    ]
  },
  {
    "id": 769,
    "english": "slow",
    "transcription": "sləʊ",
    "ru": "слоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "медленный"
      }
    ]
  },
  {
    "id": 770,
    "english": "slowly",
    "transcription": "ˈsləʊli",
    "ru": "слоули",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "медленно"
      }
    ]
  },
  {
    "id": 771,
    "english": "small",
    "transcription": "smɔːl",
    "ru": "смол",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "маленький"
      }
    ]
  },
  {
    "id": 772,
    "english": "smell",
    "transcription": "smel",
    "ru": "смэл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "запах"
      }
    ]
  },
  {
    "id": 773,
    "english": "smile",
    "transcription": "smaɪl",
    "ru": "смайл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "улыбка"
      }
    ]
  },
  {
    "id": 774,
    "english": "smirk",
    "transcription": "smɜːk",
    "ru": "смёрк",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ухмылка"
      }
    ]
  },
  {
    "id": 775,
    "english": "smoke",
    "transcription": "sməʊk",
    "ru": "смоук",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "дым"
      }
    ]
  },
  {
    "id": 776,
    "english": "snap",
    "transcription": "snæp",
    "ru": "снэп",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "щёлкать"
      }
    ]
  },
  {
    "id": 777,
    "english": "so",
    "transcription": "səʊ",
    "ru": "соу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "так"
      }
    ]
  },
  {
    "id": 778,
    "english": "soft",
    "transcription": "sɒft",
    "ru": "софт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мягкий"
      }
    ]
  },
  {
    "id": 779,
    "english": "softly",
    "transcription": "ˈsɒftli",
    "ru": "софтли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тихо"
      }
    ]
  },
  {
    "id": 780,
    "english": "some",
    "transcription": "sʌm",
    "ru": "сам",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "несколько"
      }
    ]
  },
  {
    "id": 781,
    "english": "somehow",
    "transcription": "ˈsʌmhaʊ",
    "ru": "самхау",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "как-то"
      }
    ]
  },
  {
    "id": 782,
    "english": "someone",
    "transcription": "ˈsʌmwʌn",
    "ru": "самуан",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кто-то"
      }
    ]
  },
  {
    "id": 783,
    "english": "something",
    "transcription": "ˈsʌmθɪŋ",
    "ru": "самсинг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "что-то"
      }
    ]
  },
  {
    "id": 784,
    "english": "sometimes",
    "transcription": "ˈsʌmtaɪmz",
    "ru": "самтаймз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "иногда"
      }
    ]
  },
  {
    "id": 785,
    "english": "somewhere",
    "transcription": "ˈsʌmweə",
    "ru": "самуэа",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "где-то"
      }
    ]
  },
  {
    "id": 786,
    "english": "son",
    "transcription": "sʌn",
    "ru": "сан",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сын"
      }
    ]
  },
  {
    "id": 787,
    "english": "song",
    "transcription": "sɒŋ",
    "ru": "сонг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "песня"
      }
    ]
  },
  {
    "id": 788,
    "english": "soon",
    "transcription": "suːn",
    "ru": "сун",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "скоро"
      }
    ]
  },
  {
    "id": 789,
    "english": "sorry",
    "transcription": "ˈsɒri",
    "ru": "сори",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "извините"
      }
    ]
  },
  {
    "id": 790,
    "english": "sort",
    "transcription": "sɔːt",
    "ru": "сот",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "вид"
      }
    ]
  },
  {
    "id": 791,
    "english": "sound",
    "transcription": "saʊnd",
    "ru": "саунд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "звук"
      }
    ]
  },
  {
    "id": 792,
    "english": "space",
    "transcription": "speɪs",
    "ru": "спейс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пространство"
      }
    ]
  },
  {
    "id": 793,
    "english": "speak",
    "transcription": "spiːk",
    "ru": "спик",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "говорить"
      }
    ]
  },
  {
    "id": 794,
    "english": "spend",
    "transcription": "spend",
    "ru": "спэнд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тратить"
      }
    ]
  },
  {
    "id": 795,
    "english": "spent",
    "transcription": "spent",
    "ru": "спэнт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "потратил"
      }
    ]
  },
  {
    "id": 796,
    "english": "spoke",
    "transcription": "spəʊk",
    "ru": "споук",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "говорил"
      }
    ]
  },
  {
    "id": 797,
    "english": "spot",
    "transcription": "spɒt",
    "ru": "спот",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "место"
      }
    ]
  },
  {
    "id": 798,
    "english": "stair",
    "transcription": "steə",
    "ru": "стэа",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ступенька"
      }
    ]
  },
  {
    "id": 799,
    "english": "stand",
    "transcription": "stænd",
    "ru": "стэнд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "стоять"
      }
    ]
  },
  {
    "id": 800,
    "english": "star",
    "transcription": "stɑː",
    "ru": "ста",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "звезда"
      }
    ]
  },
  {
    "id": 801,
    "english": "stare",
    "transcription": "steə",
    "ru": "стэа",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пристально смотреть"
      }
    ]
  },
  {
    "id": 802,
    "english": "start",
    "transcription": "stɑːt",
    "ru": "старт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "начинать"
      }
    ]
  },
  {
    "id": 803,
    "english": "state",
    "transcription": "steɪt",
    "ru": "стэйт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "состояние"
      }
    ]
  },
  {
    "id": 804,
    "english": "stay",
    "transcription": "steɪ",
    "ru": "стэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "оставаться"
      }
    ]
  },
  {
    "id": 805,
    "english": "step",
    "transcription": "step",
    "ru": "стэп",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "шаг"
      }
    ]
  },
  {
    "id": 806,
    "english": "stick",
    "transcription": "stɪk",
    "ru": "стик",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "палка"
      }
    ]
  },
  {
    "id": 807,
    "english": "still",
    "transcription": "stɪl",
    "ru": "стил",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "всё ещё"
      }
    ]
  },
  {
    "id": 808,
    "english": "stomach",
    "transcription": "ˈstʌmək",
    "ru": "стамэк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "живот"
      }
    ]
  },
  {
    "id": 809,
    "english": "stood",
    "transcription": "stʊd",
    "ru": "студ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "стоял"
      }
    ]
  },
  {
    "id": 810,
    "english": "stop",
    "transcription": "stɒp",
    "ru": "стоп",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "останавливаться"
      }
    ]
  },
  {
    "id": 811,
    "english": "store",
    "transcription": "stɔː",
    "ru": "стор",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "магазин"
      }
    ]
  },
  {
    "id": 812,
    "english": "story",
    "transcription": "ˈstɔːri",
    "ru": "стори",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "история"
      }
    ]
  },
  {
    "id": 813,
    "english": "straight",
    "transcription": "streɪt",
    "ru": "стрэйт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "прямой"
      }
    ]
  },
  {
    "id": 814,
    "english": "strange",
    "transcription": "streɪndʒ",
    "ru": "стрэйндж",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "странный"
      }
    ]
  },
  {
    "id": 815,
    "english": "street",
    "transcription": "striːt",
    "ru": "стрит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "улица"
      }
    ]
  },
  {
    "id": 816,
    "english": "strong",
    "transcription": "strɒŋ",
    "ru": "стронг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сильный"
      }
    ]
  },
  {
    "id": 817,
    "english": "struggle",
    "transcription": "ˈstrʌɡl",
    "ru": "страгл",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бороться"
      }
    ]
  },
  {
    "id": 818,
    "english": "stuck",
    "transcription": "stʌk",
    "ru": "стак",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "застрявший"
      }
    ]
  },
  {
    "id": 819,
    "english": "student",
    "transcription": "ˈstjuːdnt",
    "ru": "стьюдэнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "студент"
      }
    ]
  },
  {
    "id": 820,
    "english": "study",
    "transcription": "ˈstʌdi",
    "ru": "стади",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "учиться"
      }
    ]
  },
  {
    "id": 821,
    "english": "stuff",
    "transcription": "stʌf",
    "ru": "стаф",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вещи"
      }
    ]
  },
  {
    "id": 822,
    "english": "stupid",
    "transcription": "ˈstjuːpɪd",
    "ru": "стьюпид",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "глупый"
      }
    ]
  },
  {
    "id": 823,
    "english": "such",
    "transcription": "sʌtʃ",
    "ru": "сач",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "такой"
      }
    ]
  },
  {
    "id": 824,
    "english": "suck",
    "transcription": "sʌk",
    "ru": "сак",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сосать"
      }
    ]
  },
  {
    "id": 825,
    "english": "sudden",
    "transcription": "ˈsʌdn",
    "ru": "садэн",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "внезапный"
      }
    ]
  },
  {
    "id": 826,
    "english": "suddenly",
    "transcription": "ˈsʌdnli",
    "ru": "садэнли",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "внезапно"
      }
    ]
  },
  {
    "id": 827,
    "english": "suggest",
    "transcription": "səˈdʒest",
    "ru": "сэджест",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "предлагать"
      }
    ]
  },
  {
    "id": 828,
    "english": "summer",
    "transcription": "ˈsʌmə",
    "ru": "самэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "лето"
      }
    ]
  },
  {
    "id": 829,
    "english": "sun",
    "transcription": "sʌn",
    "ru": "сан",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "солнце"
      }
    ]
  },
  {
    "id": 830,
    "english": "suppose",
    "transcription": "səˈpəʊz",
    "ru": "сэпоуз",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "полагать"
      }
    ]
  },
  {
    "id": 831,
    "english": "sure",
    "transcription": "ʃʊə",
    "ru": "шуэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "уверенный"
      }
    ]
  },
  {
    "id": 832,
    "english": "surprise",
    "transcription": "səˈpraɪz",
    "ru": "сэпрайз",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сюрприз"
      }
    ]
  },
  {
    "id": 833,
    "english": "surround",
    "transcription": "səˈraʊnd",
    "ru": "сэраунд",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "окружать"
      }
    ]
  },
  {
    "id": 834,
    "english": "sweet",
    "transcription": "swiːt",
    "ru": "свит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сладкий"
      }
    ]
  },
  {
    "id": 835,
    "english": "table",
    "transcription": "ˈteɪbl",
    "ru": "тэйбл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "стол"
      }
    ]
  },
  {
    "id": 836,
    "english": "take",
    "transcription": "teɪk",
    "ru": "тэйк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "брать"
      }
    ]
  },
  {
    "id": 837,
    "english": "taken",
    "transcription": "ˈteɪkən",
    "ru": "тэйкэн",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "взятый"
      }
    ]
  },
  {
    "id": 838,
    "english": "talk",
    "transcription": "tɔːk",
    "ru": "ток",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "говорить"
      }
    ]
  },
  {
    "id": 839,
    "english": "tall",
    "transcription": "tɔːl",
    "ru": "тол",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "высокий"
      }
    ]
  },
  {
    "id": 840,
    "english": "teacher",
    "transcription": "ˈtiːtʃə",
    "ru": "тичэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "учитель"
      }
    ]
  },
  {
    "id": 841,
    "english": "team",
    "transcription": "tiːm",
    "ru": "тим",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "команда"
      }
    ]
  },
  {
    "id": 842,
    "english": "tear",
    "transcription": "tɪə",
    "ru": "тиэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "слеза"
      }
    ]
  },
  {
    "id": 843,
    "english": "teeth",
    "transcription": "tiːθ",
    "ru": "тис",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "зубы"
      }
    ]
  },
  {
    "id": 844,
    "english": "tell",
    "transcription": "tel",
    "ru": "тэл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "рассказывать"
      }
    ]
  },
  {
    "id": 845,
    "english": "ten",
    "transcription": "ten",
    "ru": "тэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "десять"
      }
    ]
  },
  {
    "id": 846,
    "english": "than",
    "transcription": "ðæn",
    "ru": "зэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "чем"
      }
    ]
  },
  {
    "id": 847,
    "english": "thank",
    "transcription": "θæŋk",
    "ru": "сэнк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "благодарить"
      }
    ]
  },
  {
    "id": 848,
    "english": "that",
    "transcription": "ðæt",
    "ru": "зэт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тот"
      }
    ]
  },
  {
    "id": 849,
    "english": "that's",
    "transcription": "ðæts",
    "ru": "зэтс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "это есть"
      }
    ]
  },
  {
    "id": 850,
    "english": "the",
    "transcription": "ðə",
    "ru": "зэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "определённый артикль"
      }
    ]
  },
  {
    "id": 851,
    "english": "their",
    "transcription": "ðeə",
    "ru": "зэа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "их"
      }
    ]
  },
  {
    "id": 852,
    "english": "them",
    "transcription": "ðem",
    "ru": "зэм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "их"
      }
    ]
  },
  {
    "id": 853,
    "english": "themselves",
    "transcription": "ðəmˈselvz",
    "ru": "зэмсэлвз",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "сами себя"
      }
    ]
  },
  {
    "id": 854,
    "english": "then",
    "transcription": "ðen",
    "ru": "зэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "затем"
      }
    ]
  },
  {
    "id": 855,
    "english": "there",
    "transcription": "ðeə",
    "ru": "зэа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "там"
      }
    ]
  },
  {
    "id": 856,
    "english": "there's",
    "transcription": "ðeəz",
    "ru": "зэаз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "там есть"
      }
    ]
  },
  {
    "id": 857,
    "english": "these",
    "transcription": "ðiːz",
    "ru": "зиз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "эти"
      }
    ]
  },
  {
    "id": 858,
    "english": "they",
    "transcription": "ðeɪ",
    "ru": "зэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "они"
      }
    ]
  },
  {
    "id": 859,
    "english": "they'd",
    "transcription": "ðeɪd",
    "ru": "зэйд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "они бы"
      }
    ]
  },
  {
    "id": 860,
    "english": "they're",
    "transcription": "ðeə",
    "ru": "зэа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "они есть"
      }
    ]
  },
  {
    "id": 861,
    "english": "thick",
    "transcription": "θɪk",
    "ru": "сик",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "толстый"
      }
    ]
  },
  {
    "id": 862,
    "english": "thing",
    "transcription": "θɪŋ",
    "ru": "синг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вещь"
      }
    ]
  },
  {
    "id": 863,
    "english": "think",
    "transcription": "θɪŋk",
    "ru": "синк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "думать"
      }
    ]
  },
  {
    "id": 864,
    "english": "third",
    "transcription": "θɜːd",
    "ru": "сёрд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "третий"
      }
    ]
  },
  {
    "id": 865,
    "english": "this",
    "transcription": "ðɪs",
    "ru": "зис",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "этот"
      }
    ]
  },
  {
    "id": 866,
    "english": "those",
    "transcription": "ðəʊz",
    "ru": "зоуз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "те"
      }
    ]
  },
  {
    "id": 867,
    "english": "though",
    "transcription": "ðəʊ",
    "ru": "зоу",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хотя"
      }
    ]
  },
  {
    "id": 868,
    "english": "thought",
    "transcription": "θɔːt",
    "ru": "сот",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мысль"
      }
    ]
  },
  {
    "id": 869,
    "english": "three",
    "transcription": "θriː",
    "ru": "сри",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "три"
      }
    ]
  },
  {
    "id": 870,
    "english": "threw",
    "transcription": "θruː",
    "ru": "сру",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бросил"
      }
    ]
  },
  {
    "id": 871,
    "english": "throat",
    "transcription": "θrəʊt",
    "ru": "сроут",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "горло"
      }
    ]
  },
  {
    "id": 872,
    "english": "through",
    "transcription": "θruː",
    "ru": "сру",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "через"
      }
    ]
  },
  {
    "id": 873,
    "english": "throw",
    "transcription": "θrəʊ",
    "ru": "сроу",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "бросать"
      }
    ]
  },
  {
    "id": 874,
    "english": "tie",
    "transcription": "taɪ",
    "ru": "тай",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "галстук"
      }
    ]
  },
  {
    "id": 875,
    "english": "tight",
    "transcription": "taɪt",
    "ru": "тайт",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тесный"
      }
    ]
  },
  {
    "id": 876,
    "english": "time",
    "transcription": "taɪm",
    "ru": "тайм",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "время"
      }
    ]
  },
  {
    "id": 877,
    "english": "tiny",
    "transcription": "ˈtaɪni",
    "ru": "тайни",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "крошечный"
      }
    ]
  },
  {
    "id": 878,
    "english": "tire",
    "transcription": "ˈtaɪə",
    "ru": "тайэ",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "уставать"
      }
    ]
  },
  {
    "id": 879,
    "english": "to",
    "transcription": "tuː",
    "ru": "ту",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "к"
      }
    ]
  },
  {
    "id": 880,
    "english": "today",
    "transcription": "təˈdeɪ",
    "ru": "тудэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сегодня"
      }
    ]
  },
  {
    "id": 881,
    "english": "together",
    "transcription": "təˈɡeðə",
    "ru": "тугэзэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вместе"
      }
    ]
  },
  {
    "id": 882,
    "english": "told",
    "transcription": "təʊld",
    "ru": "тоулд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сказал"
      }
    ]
  },
  {
    "id": 883,
    "english": "tomorrow",
    "transcription": "təˈmɒrəʊ",
    "ru": "туморроу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "завтра"
      }
    ]
  },
  {
    "id": 884,
    "english": "tone",
    "transcription": "təʊn",
    "ru": "тоун",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тон"
      }
    ]
  },
  {
    "id": 885,
    "english": "tongue",
    "transcription": "tʌŋ",
    "ru": "танг",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "язык"
      }
    ]
  },
  {
    "id": 886,
    "english": "tonight",
    "transcription": "təˈnaɪt",
    "ru": "тунайт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "сегодня вечером"
      }
    ]
  },
  {
    "id": 887,
    "english": "too",
    "transcription": "tuː",
    "ru": "ту",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тоже"
      }
    ]
  },
  {
    "id": 888,
    "english": "took",
    "transcription": "tʊk",
    "ru": "тук",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "взял"
      }
    ]
  },
  {
    "id": 889,
    "english": "top",
    "transcription": "tɒp",
    "ru": "топ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "верх"
      }
    ]
  },
  {
    "id": 890,
    "english": "totally",
    "transcription": "ˈtəʊtəli",
    "ru": "тоутэли",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "полностью"
      }
    ]
  },
  {
    "id": 891,
    "english": "touch",
    "transcription": "tʌtʃ",
    "ru": "тач",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "трогать"
      }
    ]
  },
  {
    "id": 892,
    "english": "toward",
    "transcription": "təˈwɔːd",
    "ru": "туорд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "к"
      }
    ]
  },
  {
    "id": 893,
    "english": "town",
    "transcription": "taʊn",
    "ru": "таун",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "город"
      }
    ]
  },
  {
    "id": 894,
    "english": "track",
    "transcription": "træk",
    "ru": "трэк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "след"
      }
    ]
  },
  {
    "id": 895,
    "english": "trail",
    "transcription": "treɪl",
    "ru": "трэйл",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тропа"
      }
    ]
  },
  {
    "id": 896,
    "english": "train",
    "transcription": "treɪn",
    "ru": "трэйн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "поезд"
      }
    ]
  },
  {
    "id": 897,
    "english": "tree",
    "transcription": "triː",
    "ru": "три",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дерево"
      }
    ]
  },
  {
    "id": 898,
    "english": "trip",
    "transcription": "trɪp",
    "ru": "трип",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "поездка"
      }
    ]
  },
  {
    "id": 899,
    "english": "trouble",
    "transcription": "ˈtrʌbl",
    "ru": "трабл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "проблема"
      }
    ]
  },
  {
    "id": 900,
    "english": "trust",
    "transcription": "trʌst",
    "ru": "траст",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "доверять"
      }
    ]
  },
  {
    "id": 901,
    "english": "truth",
    "transcription": "truːθ",
    "ru": "трус",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "правда"
      }
    ]
  },
  {
    "id": 902,
    "english": "try",
    "transcription": "traɪ",
    "ru": "трай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пытаться"
      }
    ]
  },
  {
    "id": 903,
    "english": "turn",
    "transcription": "tɜːn",
    "ru": "тён",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "поворачивать"
      }
    ]
  },
  {
    "id": 904,
    "english": "tv",
    "transcription": "ˌtiːˈviː",
    "ru": "тиви",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "телевизор"
      }
    ]
  },
  {
    "id": 905,
    "english": "twenty",
    "transcription": "ˈtwenti",
    "ru": "твэнти",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "двадцать"
      }
    ]
  },
  {
    "id": 906,
    "english": "two",
    "transcription": "tuː",
    "ru": "ту",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "два"
      }
    ]
  },
  {
    "id": 907,
    "english": "type",
    "transcription": "taɪp",
    "ru": "тайп",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "тип"
      }
    ]
  },
  {
    "id": 908,
    "english": "uncle",
    "transcription": "ˈʌŋkl",
    "ru": "анкл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "дядя"
      }
    ]
  },
  {
    "id": 909,
    "english": "under",
    "transcription": "ˈʌndə",
    "ru": "андэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "под"
      }
    ]
  },
  {
    "id": 910,
    "english": "understand",
    "transcription": "ˌʌndəˈstænd",
    "ru": "андэстэнд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "понимать"
      }
    ]
  },
  {
    "id": 911,
    "english": "until",
    "transcription": "ənˈtɪl",
    "ru": "антил",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "до, пока"
      }
    ]
  },
  {
    "id": 912,
    "english": "up",
    "transcription": "ʌp",
    "ru": "ап",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вверх"
      }
    ]
  },
  {
    "id": 913,
    "english": "upon",
    "transcription": "əˈpɒn",
    "ru": "апон",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "на"
      }
    ]
  },
  {
    "id": 914,
    "english": "us",
    "transcription": "ʌs",
    "ru": "ас",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "нас"
      }
    ]
  },
  {
    "id": 915,
    "english": "use",
    "transcription": "juːz",
    "ru": "юз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "использовать"
      }
    ]
  },
  {
    "id": 916,
    "english": "usual",
    "transcription": "ˈjuːʒuəl",
    "ru": "южуал",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "обычный"
      }
    ]
  },
  {
    "id": 917,
    "english": "usually",
    "transcription": "ˈjuːʒuəli",
    "ru": "южуали",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "обычно"
      }
    ]
  },
  {
    "id": 918,
    "english": "very",
    "transcription": "ˈveri",
    "ru": "вэри",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "очень"
      }
    ]
  },
  {
    "id": 919,
    "english": "visit",
    "transcription": "ˈvɪzɪt",
    "ru": "визит",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "посещать"
      }
    ]
  },
  {
    "id": 920,
    "english": "voice",
    "transcription": "vɔɪs",
    "ru": "войс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "голос"
      }
    ]
  },
  {
    "id": 921,
    "english": "wait",
    "transcription": "weɪt",
    "ru": "уэйт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ждать"
      }
    ]
  },
  {
    "id": 922,
    "english": "wake",
    "transcription": "weɪk",
    "ru": "уэйк",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "просыпаться"
      }
    ]
  },
  {
    "id": 923,
    "english": "walk",
    "transcription": "wɔːk",
    "ru": "уок",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "идти"
      }
    ]
  },
  {
    "id": 924,
    "english": "wall",
    "transcription": "wɔːl",
    "ru": "уол",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "стена"
      }
    ]
  },
  {
    "id": 925,
    "english": "want",
    "transcription": "wɒnt",
    "ru": "уонт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хотеть"
      }
    ]
  },
  {
    "id": 926,
    "english": "warm",
    "transcription": "wɔːm",
    "ru": "уом",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "тёплый"
      }
    ]
  },
  {
    "id": 927,
    "english": "warn",
    "transcription": "wɔːn",
    "ru": "уон",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "предупреждать"
      }
    ]
  },
  {
    "id": 928,
    "english": "was",
    "transcription": "wɒz",
    "ru": "уоз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "был"
      }
    ]
  },
  {
    "id": 929,
    "english": "wasn't",
    "transcription": "ˈwɒznt",
    "ru": "уознт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не был"
      }
    ]
  },
  {
    "id": 930,
    "english": "watch",
    "transcription": "wɒtʃ",
    "ru": "уотч",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "смотреть"
      }
    ]
  },
  {
    "id": 931,
    "english": "water",
    "transcription": "ˈwɔːtə",
    "ru": "уотэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вода"
      }
    ]
  },
  {
    "id": 932,
    "english": "wave",
    "transcription": "weɪv",
    "ru": "уэйв",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "волна"
      }
    ]
  },
  {
    "id": 933,
    "english": "way",
    "transcription": "weɪ",
    "ru": "уэй",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "путь"
      }
    ]
  },
  {
    "id": 934,
    "english": "we",
    "transcription": "wiː",
    "ru": "уи",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мы"
      }
    ]
  },
  {
    "id": 935,
    "english": "we'll",
    "transcription": "wiːl",
    "ru": "уил",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мы будем"
      }
    ]
  },
  {
    "id": 936,
    "english": "we're",
    "transcription": "wɪə",
    "ru": "уиэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мы есть"
      }
    ]
  },
  {
    "id": 937,
    "english": "we've",
    "transcription": "wiːv",
    "ru": "уив",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мы имеем"
      }
    ]
  },
  {
    "id": 938,
    "english": "wear",
    "transcription": "weə",
    "ru": "уэа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "носить"
      }
    ]
  },
  {
    "id": 939,
    "english": "week",
    "transcription": "wiːk",
    "ru": "уик",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "неделя"
      }
    ]
  },
  {
    "id": 940,
    "english": "weird",
    "transcription": "wɪəd",
    "ru": "уиэд",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "странный"
      }
    ]
  },
  {
    "id": 941,
    "english": "well",
    "transcription": "wel",
    "ru": "уэл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "хорошо"
      }
    ]
  },
  {
    "id": 942,
    "english": "went",
    "transcription": "went",
    "ru": "уэнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "пошёл"
      }
    ]
  },
  {
    "id": 943,
    "english": "were",
    "transcription": "wɜː",
    "ru": "уё",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "были"
      }
    ]
  },
  {
    "id": 944,
    "english": "weren't",
    "transcription": "wɜːnt",
    "ru": "уёнт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не были"
      }
    ]
  },
  {
    "id": 945,
    "english": "wet",
    "transcription": "wet",
    "ru": "уэт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "мокрый"
      }
    ]
  },
  {
    "id": 946,
    "english": "what",
    "transcription": "wɒt",
    "ru": "уот",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "что"
      }
    ]
  },
  {
    "id": 947,
    "english": "what's",
    "transcription": "wɒts",
    "ru": "уотс",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "что есть"
      }
    ]
  },
  {
    "id": 948,
    "english": "whatever",
    "transcription": "wɒtˈevə",
    "ru": "уотэвэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "что угодно"
      }
    ]
  },
  {
    "id": 949,
    "english": "when",
    "transcription": "wen",
    "ru": "уэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "когда"
      }
    ]
  },
  {
    "id": 950,
    "english": "where",
    "transcription": "weə",
    "ru": "уэа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "где"
      }
    ]
  },
  {
    "id": 951,
    "english": "whether",
    "transcription": "ˈweðə",
    "ru": "уэзэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ли"
      }
    ]
  },
  {
    "id": 952,
    "english": "which",
    "transcription": "wɪtʃ",
    "ru": "уич",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "который"
      }
    ]
  },
  {
    "id": 953,
    "english": "while",
    "transcription": "waɪl",
    "ru": "уайл",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "пока"
      }
    ]
  },
  {
    "id": 954,
    "english": "whisper",
    "transcription": "ˈwɪspə",
    "ru": "уиспэ",
    "level": "B2",
    "topic": "general",
    "meanings": [
      {
        "russian": "шептать"
      }
    ]
  },
  {
    "id": 955,
    "english": "white",
    "transcription": "waɪt",
    "ru": "уайт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "белый"
      }
    ]
  },
  {
    "id": 956,
    "english": "who",
    "transcription": "huː",
    "ru": "ху",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кто"
      }
    ]
  },
  {
    "id": 957,
    "english": "whole",
    "transcription": "həʊl",
    "ru": "хоул",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "целый"
      }
    ]
  },
  {
    "id": 958,
    "english": "why",
    "transcription": "waɪ",
    "ru": "уай",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "почему"
      }
    ]
  },
  {
    "id": 959,
    "english": "wide",
    "transcription": "waɪd",
    "ru": "уайд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "широкий"
      }
    ]
  },
  {
    "id": 960,
    "english": "wife",
    "transcription": "waɪf",
    "ru": "уайф",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "жена"
      }
    ]
  },
  {
    "id": 961,
    "english": "will",
    "transcription": "wɪl",
    "ru": "уил",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "будет"
      }
    ]
  },
  {
    "id": 962,
    "english": "wind",
    "transcription": "wɪnd",
    "ru": "уинд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ветер"
      }
    ]
  },
  {
    "id": 963,
    "english": "window",
    "transcription": "ˈwɪndəʊ",
    "ru": "уиндоу",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "окно"
      }
    ]
  },
  {
    "id": 964,
    "english": "wipe",
    "transcription": "waɪp",
    "ru": "уайп",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вытирать"
      }
    ]
  },
  {
    "id": 965,
    "english": "wish",
    "transcription": "wɪʃ",
    "ru": "уиш",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "желать"
      }
    ]
  },
  {
    "id": 966,
    "english": "with",
    "transcription": "wɪð",
    "ru": "уиз",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "с"
      }
    ]
  },
  {
    "id": 967,
    "english": "within",
    "transcription": "wɪˈðɪn",
    "ru": "уизин",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "внутри"
      }
    ]
  },
  {
    "id": 968,
    "english": "without",
    "transcription": "wɪˈðaʊt",
    "ru": "уизаут",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "без"
      }
    ]
  },
  {
    "id": 969,
    "english": "woke",
    "transcription": "wəʊk",
    "ru": "уоук",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "проснулся"
      }
    ]
  },
  {
    "id": 970,
    "english": "woman",
    "transcription": "ˈwʊmən",
    "ru": "уумэн",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "женщина"
      }
    ]
  },
  {
    "id": 971,
    "english": "women",
    "transcription": "ˈwɪmɪn",
    "ru": "уимин",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "женщины"
      }
    ]
  },
  {
    "id": 972,
    "english": "won't",
    "transcription": "wəʊnt",
    "ru": "уоунт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "не будет"
      }
    ]
  },
  {
    "id": 973,
    "english": "wonder",
    "transcription": "ˈwʌndə",
    "ru": "уандэ",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "удивляться"
      }
    ]
  },
  {
    "id": 974,
    "english": "wood",
    "transcription": "wʊd",
    "ru": "вуд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "дерево"
      }
    ]
  },
  {
    "id": 975,
    "english": "word",
    "transcription": "wɜːd",
    "ru": "уёд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "слово"
      }
    ]
  },
  {
    "id": 976,
    "english": "wore",
    "transcription": "wɔː",
    "ru": "уо",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "носил"
      }
    ]
  },
  {
    "id": 977,
    "english": "work",
    "transcription": "wɜːk",
    "ru": "уёк",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "работать"
      }
    ]
  },
  {
    "id": 978,
    "english": "world",
    "transcription": "wɜːld",
    "ru": "уёлд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "мир"
      }
    ]
  },
  {
    "id": 979,
    "english": "worry",
    "transcription": "ˈwʌri",
    "ru": "уари",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "беспокоиться"
      }
    ]
  },
  {
    "id": 980,
    "english": "worse",
    "transcription": "wɜːs",
    "ru": "уёс",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "хуже"
      }
    ]
  },
  {
    "id": 981,
    "english": "would",
    "transcription": "wʊd",
    "ru": "вуд",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "бы"
      }
    ]
  },
  {
    "id": 982,
    "english": "wouldn't",
    "transcription": "ˈwʊdnt",
    "ru": "вуднт",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "не бы"
      }
    ]
  },
  {
    "id": 983,
    "english": "wow",
    "transcription": "waʊ",
    "ru": "уау",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "вау"
      }
    ]
  },
  {
    "id": 984,
    "english": "wrap",
    "transcription": "ræp",
    "ru": "рэп",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "заворачивать"
      }
    ]
  },
  {
    "id": 985,
    "english": "write",
    "transcription": "raɪt",
    "ru": "райт",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "писать"
      }
    ]
  },
  {
    "id": 986,
    "english": "wrong",
    "transcription": "rɒŋ",
    "ru": "ронг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "неправильный"
      }
    ]
  },
  {
    "id": 987,
    "english": "yeah",
    "transcription": "jeə",
    "ru": "йеа",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "да"
      }
    ]
  },
  {
    "id": 988,
    "english": "year",
    "transcription": "jɪə",
    "ru": "йиэ",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "год"
      }
    ]
  },
  {
    "id": 989,
    "english": "yell",
    "transcription": "jel",
    "ru": "йел",
    "level": "B1",
    "topic": "general",
    "meanings": [
      {
        "russian": "кричать"
      }
    ]
  },
  {
    "id": 990,
    "english": "yes",
    "transcription": "jes",
    "ru": "йес",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "да"
      }
    ]
  },
  {
    "id": 991,
    "english": "yet",
    "transcription": "jet",
    "ru": "йет",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ещё"
      }
    ]
  },
  {
    "id": 992,
    "english": "you",
    "transcription": "juː",
    "ru": "ю",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ты"
      }
    ]
  },
  {
    "id": 993,
    "english": "you'd",
    "transcription": "juːd",
    "ru": "юд",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ты бы"
      }
    ]
  },
  {
    "id": 994,
    "english": "you'll",
    "transcription": "juːl",
    "ru": "юл",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ты будешь"
      }
    ]
  },
  {
    "id": 995,
    "english": "you're",
    "transcription": "jɔː",
    "ru": "йо",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "ты есть"
      }
    ]
  },
  {
    "id": 996,
    "english": "you've",
    "transcription": "juːv",
    "ru": "юв",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "ты имеешь"
      }
    ]
  },
  {
    "id": 997,
    "english": "young",
    "transcription": "jʌŋ",
    "ru": "янг",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "молодой"
      }
    ]
  },
  {
    "id": 998,
    "english": "your",
    "transcription": "jɔː",
    "ru": "йо",
    "level": "A1",
    "topic": "general",
    "meanings": [
      {
        "russian": "твой"
      }
    ]
  },
  {
    "id": 999,
    "english": "yourself",
    "transcription": "jɔːˈself",
    "ru": "йосэлф",
    "level": "A2",
    "topic": "general",
    "meanings": [
      {
        "russian": "себя"
      }
    ]
  }
]
