from __future__ import annotations

from aiogram import Router, F
from aiogram.types import Message

from containers import Container
from keyboards.main_kb import progress_kb
from presenters import progress_view

router = Router()


@router.message(F.text == "📊 Прогресс")
async def show_progress(message: Message, container: Container) -> None:
    uid = message.from_user.id
    summary = await container.progress.summary(uid)
    srs = await container.srs.progress(uid)
    level = (await container.settings.get(uid)).level
    await message.answer(progress_view(summary, srs, level), reply_markup=progress_kb(srs["due"]))
