from __future__ import annotations

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import callbacks as cb
from keyboards.main_kb import main_menu_kb, MENU_TEXT

router = Router()

_WELCOME = (
    "👋 <b>Привет!</b> Я помогу учить английский.\n\n"
    "📝 <b>Тесты</b> — слова, глаголы и предложения на время\n"
    "🎧 <b>Аудирование</b> — тексты с озвучкой и переводом\n"
    "🗣 <b>Говорение</b> — скоро\n"
    "⚙️ <b>Настройки</b> — сложность, время, голос озвучки\n\n"
    "Выбери раздел в меню ниже 👇"
)


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(_WELCOME, reply_markup=main_menu_kb())


@router.message(F.text == "🗣 Говорение")
async def speaking_soon(message: Message) -> None:
    await message.answer(
        "🗣 <b>Говорение</b>\n\n"
        "🔜 Скоро: отправляешь голосовое — бот распознаёт речь и проверяет произношение."
    )


@router.message(F.text == MENU_TEXT)
async def menu_button(message: Message) -> None:
    await message.answer("🏠 Главное меню", reply_markup=main_menu_kb())


@router.callback_query(F.data == cb.MAIN_MENU)
async def back_to_main(callback: CallbackQuery) -> None:
    await callback.message.answer("🏠 Главное меню", reply_markup=main_menu_kb())
    await callback.answer()
