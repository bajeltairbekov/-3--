import sqlite3

def create_tables():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            category TEXT,
            size TEXT,
            price REAL,
            article TEXT,
            photo BLOB
        )
    ''')


    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()