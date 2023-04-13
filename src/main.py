from aiogram import executor

import commands  # NOQA
from core import dp, settings
from middleware.register_user import RegisterUserMiddleware


def main():
    dp.middleware.setup(RegisterUserMiddleware())
    executor.start_polling(dp, skip_updates=settings.LOCAL)


if __name__ == "__main__":
    main()
