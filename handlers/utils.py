"""Мелкие переиспользуемые утилиты хендлеров (DRY)."""
from __future__ import annotations

import logging

from aiogram import Bot
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

logger = logging.getLogger(__name__)


def _is_not_modified(error: Exception) -> bool:
    return "message is not modified" in str(error)


async def safe_edit(message: Message, text: str, reply_markup=None) -> None:
    """edit_text по объекту Message, игнорируя ошибку «message is not modified».

    Telegram падает, если новое содержимое идентично текущему (напр. «Дальше»
    выпало то же слово или выбран тот же счётчик). Для пользователя это не ошибка.
    """
    try:
        await message.edit_text(text, reply_markup=reply_markup)
    except TelegramBadRequest as e:
        if not _is_not_modified(e):
            raise


async def safe_edit_by_id(bot: Bot, chat_id: int, message_id: int, text: str, reply_markup=None) -> None:
    """edit_message_text по chat_id+message_id (когда объекта Message нет под рукой).

    Устойчива: любые ошибки правки логируются и гасятся — правка второстепенна и
    не должна ронять поток (напр. отметка отвеченного вопроса в тесте).
    """
    try:
        await bot.edit_message_text(text, chat_id=chat_id, message_id=message_id, reply_markup=reply_markup)
    except Exception:
        logger.exception("Не удалось отредактировать сообщение %s/%s", chat_id, message_id)
