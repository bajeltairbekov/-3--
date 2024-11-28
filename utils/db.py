import sqlite3

def add_product_to_db(product_data):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            size TEXT,
            price REAL,
            article TEXT,
            photo TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO products (name, category, size, price, article, photo)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (product_data['name'], product_data['category'], product_data['size'],
          product_data['price'], product_data['article'], product_data['photo']))

    conn.commit()
    conn.close()