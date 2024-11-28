from aiogram import types
from aiogram.dispatcher import Dispatcher


async def cmd_info(message: types.Message):
    info_text = """
    Этот бот предназначен для оформления заказов. Вы можете использовать следующие команды:
    - /start — начать работу с ботом.
    - /products — увидеть все доступные товары.
    - /order — оформить заказ.
    """
    await message.answer(info_text)
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_info, commands=["info"])