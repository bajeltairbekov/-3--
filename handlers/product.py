from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.types import ContentType
import sqlite3





def get_all_products():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, price, size FROM products')
    products = cursor.fetchall()
    conn.close()
    return [{'name': row[0], 'price': row[1], 'size': row[2]} for row in products]

async def cmd_products(message: types.Message):
    products = get_all_products()
    if products:
        for product in products:
            await message.answer(f"Товар: {product['name']}\nЦена: {product['price']}\nРазмер: {product['size']}")
    else:
        await message.answer("Нет товаров в базе.")


class ProductForm(StatesGroup):
    name = State()
    size = State()
    price = State()
    article = State()
    photo = State()



async def cmd_add_product(message: types.Message):
    await message.answer("Введите название товара:")
    await ProductForm.name.set()



async def process_name(message: types.Message, state):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Введите категорию товара:")
    await ProductForm.category.set()



async def process_category(message: types.Message, state):
    async with state.proxy() as data:
        data['category'] = message.text
    await message.answer("Введите размер товара:")
    await ProductForm.size.set()


async def process_size(message: types.Message, state):
    async with state.proxy() as data:
        data['size'] = message.text
    await message.answer("Введите цену товара:")
    await ProductForm.price.set()



async def process_price(message: types.Message, state):
    async with state.proxy() as data:
        data['price'] = message.text
    await message.answer("Введите артикул товара:")
    await ProductForm.article.set()


async def process_article(message: types.Message, state):
    async with state.proxy() as data:
        data['article'] = message.text
    await message.answer("Пожалуйста, отправьте фото товара:")
    await ProductForm.photo.set()


async def process_photo(message: types.Message, state):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id

        save_product_to_db(data)

    await message.answer("Товар успешно добавлен!")
    await state.finish()


def save_product_to_db(data):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()


    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (name TEXT, category TEXT, size TEXT, price TEXT, article TEXT, photo TEXT)''')


    c.execute("INSERT INTO products (name, category, size, price, article, photo) VALUES (?, ?, ?, ?, ?, ?)",
              (data['name'], data['category'], data['size'], data['price'], data['article'], data['photo']))

    conn.commit()
    conn.close()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_add_product, commands=["add_product"])
    dp.register_message_handler(process_name, state=ProductForm.name)
    dp.register_message_handler(process_category, state=ProductForm.category)
    dp.register_message_handler(process_size, state=ProductForm.size)
    dp.register_message_handler(process_price, state=ProductForm.price)
    dp.register_message_handler(process_article, state=ProductForm.article)
    dp.register_message_handler(process_photo, state=ProductForm.photo, content_types=ContentType.PHOTO)
    dp.register_message_handler(cmd_products, commands=["products"])