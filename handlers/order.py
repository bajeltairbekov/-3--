from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text

# Определение состояний для процесса оформления заказа
class OrderForm(StatesGroup):
    article = State()  # артикул товара
    size = State()  # размер
    quantity = State()  # количество
    contact = State()  # контактные данные (телефон)

# Команда для начала оформления заказа
async def cmd_order(message: types.Message):
    await message.answer("Введите артикул товара, который хотите заказать:")
    await OrderForm.article.set()  # Устанавливаем состояние для артикля товара

# Обработчик для ввода артикля товара
async def process_article(message: types.Message, state):
    async with state.proxy() as data:
        data['article'] = message.text  # Сохраняем артикул
    await message.answer("Введите размер товара:")
    await OrderForm.size.set()  # Переходим к следующему состоянию

# Обработчик для ввода размера
async def process_size(message: types.Message, state):
    async with state.proxy() as data:
        data['size'] = message.text  # Сохраняем размер
    await message.answer("Введите количество товара:")
    await OrderForm.quantity.set()  # Переходим к следующему состоянию

# Обработчик для ввода количества
async def process_quantity(message: types.Message, state):
    async with state.proxy() as data:
        data['quantity'] = message.text  # Сохраняем количество
    await message.answer("Введите ваш номер телефона:")
    await OrderForm.contact.set()  # Переходим к следующему состоянию

# Обработчик для ввода контакта (телефон)
async def process_contact(message: types.Message, state):
    async with state.proxy() as data:
        data['contact'] = message.text
        if len(data['contact']) < 10:
            await message.answer("Пожалуйста, введите корректный номер телефона.")
            return  # Повторно попросим пользователя ввести номер

        # Отправляем заказ сотрудникам (можно организовать отправку на email, в другой чат, или в список staff)
        staff_list = [1253330340]  # Пример списка сотрудников
        order_info = f"Новый заказ:\nАртикул: {data['article']}\nРазмер: {data['size']}\nКоличество: {data['quantity']}\nКонтакт: {data['contact']}"
        for staff_id in staff_list:
            await message.bot.send_message(staff_id, order_info)

    await message.answer("Ваш заказ оформлен! Мы свяжемся с вами.")
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_order, commands=["order"])
    dp.register_message_handler(process_article, state=OrderForm.article)
    dp.register_message_handler(process_size, state=OrderForm.size)
    dp.register_message_handler(process_quantity, state=OrderForm.quantity)
    dp.register_message_handler(process_contact, state=OrderForm.contact)