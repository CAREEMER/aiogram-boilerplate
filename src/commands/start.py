from aiogram import types

from core import dp


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    credentials = message.from_user.username if message.from_user.username else message.from_user.first_name
    await message.reply(f"Привет, {credentials}! Используй команду /get_cats")
