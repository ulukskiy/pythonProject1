# import sqlite3
# def creat_connection(hw):
#     try:
#         connection = sqlite3.connect(hw)
#         return connection
#     except sqlite3.Error as e:
#         print(e)
# def create_table(connection, sql):
#     """Создает таблицу"""
#     try:
#         cursor = connection.cursor()
#         cursor.execute(sql)
#     except sqlite3.Error as e:
#         print(e)
#
# connection=creat_connection("hw.db")
#
# sql_creat_products_table = '''
# CREAT TABLE products{
#     id INTEGER PRIMARY KEY,
#     product_title TEXT NOT NULL,
#     price NUMERIC(10, 2) DEFAULT 0.0 NOT NULL,
#     quantity INTEGER DEFAULT 0 NOT NULL
#     }
#
#
# '''
#
#
# if connection:
#     print('Соединение с БД установлено')
#
# connection.close()
#
#
import sqlite3

def create_database():
    conn = sqlite3.connect("hw.db")
    conn.close()

def create_product_table():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                  id INTEGER PRIMARY KEY,
                  product_title TEXT NOT NULL,
                  price NUMERIC(10, 2) DEFAULT 0.0 NOT NULL,
                  quantity INTEGER DEFAULT 0 NOT NULL
              )''')
    conn.commit()
    conn.close()

def add_product(product_title, price=0.0, quantity=0):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", (product_title, price, quantity))
    conn.commit()
    conn.close()

def update_quantity_by_id(product_id, new_quantity):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()

def update_price_by_id(product_id, new_price):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()

def delete_product_by_id(product_id):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def select_all_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

def select_cheap_and_abundant_products():
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE price < 100 AND quantity > 5")
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

#  Функция для поиска товаров по названию
def search_products_by_title(keyword):
    conn = sqlite3.connect("hw.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE product_title LIKE ?", ('%' + keyword + '%',))
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

# Тестирование функций
create_database()
create_product_table()

add_product("Жидкое мыло с запахом ванили", 4.99, 10)
add_product("Мыло детское", 3.49, 15)

print("Все товары:")
select_all_products()

print("Дешевле 100 сомов и больше 5 штук:")
select_cheap_and_abundant_products()

print("Поиск по слову 'мыло':")
search_products_by_title("мыло")

