from aiogram import types
from aiogram.filters import CommandStart

from core.bot import dp


@dp.message(CommandStart())
async def process_start_command(message: types.Message):
    credentials = message.from_user.username if message.from_user.username else message.from_user.first_name
    await message.reply(f"Привет, {credentials}!")
