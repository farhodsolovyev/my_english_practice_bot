from __future__ import annotations

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

import callbacks as cb
from containers import Container
from keyboards.main_kb import (
    settings_menu_kb, settings_level_kb, settings_time_kb, settings_size_kb, settings_voice_kb,
)
from presenters import settings_view
from handlers.utils import safe_edit

router = Router()

# cb-поле → (поле модели, клавиатура выбора, заголовок)
_FIELD_MAP = {
    "level": ("level", settings_level_kb, "🎚 <b>Сложность</b>\nКакие слова показывать в тестах:"),
    "time": ("quiz_seconds", settings_time_kb, "⏱ <b>Время на ответ</b>\nСколько секунд на вопрос:"),
    "size": ("quiz_size", settings_size_kb, "🔢 <b>Вопросов в тесте</b>\nДлина одной сессии:"),
    "voice": ("voice", settings_voice_kb, "🔊 <b>Голос озвучки</b>\nАкцент и пол диктора:"),
}


def _cast(model_field: str, raw: str):
    if raw == "none":
        return None
    if model_field in ("quiz_seconds", "quiz_size"):
        return int(raw)
    return raw  # level ("A1"..) или voice (short name)


@router.message(F.text == "⚙️ Настройки")
async def open_settings(message: Message, container: Container) -> None:
    s = await container.settings.get(message.from_user.id)
    await message.answer(settings_view(s), reply_markup=settings_menu_kb())


@router.callback_query(F.data == cb.SETTINGS_MENU)
async def settings_root(callback: CallbackQuery, container: Container) -> None:
    s = await container.settings.get(callback.from_user.id)
    await safe_edit(callback.message, settings_view(s), settings_menu_kb())
    await callback.answer()


@router.callback_query(F.data.in_(cb.SETTING_OPEN_ALL))
async def open_chooser(callback: CallbackQuery, container: Container) -> None:
    _model_field, kb, title = _FIELD_MAP[cb.parse_setting_open(callback.data)]
    s = await container.settings.get(callback.from_user.id)
    await safe_edit(callback.message, title, kb(s))
    await callback.answer()


@router.callback_query(lambda c: cb.is_setting_apply(c.data))
async def apply_setting(callback: CallbackQuery, container: Container) -> None:
    field, raw = cb.parse_setting_apply(callback.data)
    model_field = _FIELD_MAP[field][0]
    try:
        s = await container.settings.update(callback.from_user.id, model_field, _cast(model_field, raw))
    except ValueError:
        await callback.answer("Неизвестное значение", show_alert=True)
        return
    await safe_edit(callback.message, settings_view(s), settings_menu_kb())
    await callback.answer("✅ Сохранено")


# ─── Адаптив: применение предложения сменить уровень ─────────────────────────
@router.callback_query(F.data.startswith(cb.LEVEL_SET))
async def level_apply(callback: CallbackQuery, container: Container) -> None:
    level = cb.parse_level_set(callback.data)
    await container.settings.update(callback.from_user.id, "level", level)
    await container.stats.reset(callback.from_user.id, level)  # свежий отсчёт на новом уровне
    await safe_edit(callback.message, f"✅ Сложность изменена на <b>{level}</b>. Продолжаем 💪", None)
    await callback.answer("Готово")


@router.callback_query(F.data == cb.LEVEL_KEEP)
async def level_keep(callback: CallbackQuery, container: Container) -> None:
    s = await container.settings.get(callback.from_user.id)
    await container.stats.reset(callback.from_user.id, s.level)  # не предлагать снова сразу
    await safe_edit(callback.message, "Ок, оставляем текущий уровень 👍", None)
    await callback.answer()
