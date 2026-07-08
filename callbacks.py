"""Единый формат callback_data: сборка (для кнопок) и разбор (для хендлеров).

Один источник правды по «проводному» формату колбэков — вместо магических строк
и хрупких `split(":")[n]` по всему коду. Формат строк не меняется.
"""
from __future__ import annotations

# ── фиксированные колбэки ──
MAIN_MENU = "main_menu"
NOOP = "noop"
LISTEN_LEVELS = "lst:levels"
SETTINGS_MENU = "set:menu"
LEVEL_KEEP = "lvl:keep"

# ── префиксы параметрических колбэков ──
QUIZ_PICK = "qz:"
ANSWER = "ans:"
LISTEN_LEVEL = "lst:lvl:"
LISTEN_OPEN = "lst:open:"
LEVEL_SET = "lvl:set:"
_SETTING = "set:"

SETTING_FIELDS = ["level", "time", "size", "voice"]
SETTING_OPEN_ALL = [f"{_SETTING}{f}" for f in SETTING_FIELDS]          # ["set:level", ...]
SETTING_APPLY_PREFIXES = [f"{_SETTING}{f}:v:" for f in SETTING_FIELDS]  # ["set:level:v:", ...]


# ── сборка (для клавиатур) ──
def quiz_pick(section: str) -> str:
    return f"{QUIZ_PICK}{section}"


def answer(qid: int, option: int) -> str:
    return f"{ANSWER}{qid}:{option}"


def listen_level(level: str) -> str:
    return f"{LISTEN_LEVEL}{level}"


def listen_open(text_id: int) -> str:
    return f"{LISTEN_OPEN}{text_id}"


def level_set(level: str) -> str:
    return f"{LEVEL_SET}{level}"


def setting_open(field: str) -> str:
    return f"{_SETTING}{field}"


def setting_apply(field: str, value) -> str:
    return f"{_SETTING}{field}:v:{value}"


# ── разбор (для хендлеров) ──
def parse_quiz_pick(data: str) -> str:
    return data[len(QUIZ_PICK):]


def parse_answer(data: str) -> tuple[int, int]:
    _, qid, opt = data.split(":")
    return int(qid), int(opt)


def parse_listen_level(data: str) -> str:
    return data[len(LISTEN_LEVEL):]


def parse_listen_open(data: str) -> int:
    return int(data[len(LISTEN_OPEN):])


def parse_level_set(data: str) -> str:
    return data[len(LEVEL_SET):]


def parse_setting_open(data: str) -> str:
    return data[len(_SETTING):]


def parse_setting_apply(data: str) -> tuple[str, str]:
    _, field, _v, value = data.split(":")
    return field, value


def is_setting_apply(data: str | None) -> bool:
    return bool(data) and any(data.startswith(p) for p in SETTING_APPLY_PREFIXES)
