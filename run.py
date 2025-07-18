import asyncio
import os
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import router


async def main():
    load_dotenv()
    bot = Bot(token = os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Бот запущен')
        asyncio.run(main())
    except:
        print('Бот выключен')