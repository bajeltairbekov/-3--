from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN
from handlers import product
from handlers import start, info, product, order
import logging
from decouple import config




token = config('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())


product.register_handlers(dp)
info.register_handlers(dp)
start.register_handlers(dp)
order.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)