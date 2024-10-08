from typing import Any, Awaitable, Callable, Dict

from aiogram.types import Update

from core.bot import dp
from core.db import async_session
from services.telegram_user.get_or_create import get_or_create_user


@dp.update.outer_middleware()
async def register_user(
    handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
    update: Update,
    data: dict[str, Any],
):
    async with async_session() as session:
        data["user"] = await get_or_create_user(update.event.from_user, session)

    await handler(update, data)
