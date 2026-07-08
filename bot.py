from __future__ import annotations

import asyncio
import datetime
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from containers import build_container, Container
from handlers import (
    start, quiz_flow, listening, settings as settings_handler, progress, fallback,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
)
logger = logging.getLogger(__name__)


async def _reminder_loop(bot: Bot, container: Container) -> None:
    """Раз в день в settings.reminder_hour пингует тех, у кого есть слова к повторению."""
    while True:
        try:
            now = datetime.datetime.now()
            target = now.replace(hour=settings.reminder_hour, minute=0, second=0, microsecond=0)
            if target <= now:
                target += datetime.timedelta(days=1)
            await asyncio.sleep((target - now).total_seconds())

            for uid in await container.srs.users_with_due():
                due = len(await container.srs.due_ids(uid))
                if not due:
                    continue
                try:
                    await bot.send_message(
                        uid,
                        f"🔁 <b>{due} слов ждут повторения</b>\n"
                        "Пара минут сейчас — и они останутся в памяти 💪\n"
                        "Открой «📝 Тесты» → 🔁 Повторение.",
                    )
                except Exception:
                    logger.warning("Не удалось отправить напоминание %s", uid)
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception("Сбой цикла напоминаний")
            await asyncio.sleep(3600)


async def main() -> None:
    container = build_container()

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp["container"] = container  # доступно хендлерам как аргумент `container`

    # fallback — последним: ловит всё необработанное (старые кнопки и т.п.)
    for module in (start, quiz_flow, listening, settings_handler, progress, fallback):
        dp.include_router(module.router)

    asyncio.create_task(_reminder_loop(bot, container))  # ежедневные напоминания

    logger.info("🤖 Бот запущен!")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
