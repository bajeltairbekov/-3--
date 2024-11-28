from aiogram.dispatcher.filters.state import State, StatesGroup

class ProductForm(StatesGroup):
    name = State()
    category = State()
    size = State()
    price = State()
    sku = State()
    photo = State()