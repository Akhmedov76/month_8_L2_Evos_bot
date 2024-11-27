import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from main.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("bot.log", mode="a")
    ]
)

logger = logging.getLogger(__name__)

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Bot ishga tushirilayotganda xato yuz berdi: {e}")

if __name__ == "__main__":
    asyncio.run(main())
