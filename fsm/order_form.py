from aiogram.dispatcher.filters.state import State, StatesGroup

class OrderForm(StatesGroup):
    sku = State()
    size = State()
    quantity = State()
    contact = State()