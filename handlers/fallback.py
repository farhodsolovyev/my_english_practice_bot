"""Подстраховка: ловит всё, что не поймали разделы.

Решает частую проблему — у пользователя в чате осталась СТАРАЯ reply-клавиатура
или старые inline-кнопки от прежней версии. Регистрируется ПОСЛЕДНИМ.
"""
from __future__ import annotations

from aiogram import Router
from aiogram.types import Message, CallbackQuery

from keyboards.main_kb import main_menu_kb

router = Router()


@router.message()
async def unknown_message(message: Message) -> None:
    await message.answer("🤔 Не понял. Вот актуальное меню 👇", reply_markup=main_menu_kb())


@router.callback_query()
async def unknown_callback(callback: CallbackQuery) -> None:
    await callback.answer("Эта кнопка устарела. Нажми /start, чтобы обновить меню.", show_alert=True)
