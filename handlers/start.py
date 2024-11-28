
from aiogram import types
from aiogram.dispatcher import Dispatcher


async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для оформления заказов. Используйте /products для просмотра товаров."
                         "/add_product для добавления товара")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])