import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('coffee.sqlite')
cur = conn.cursor()

# Получение информации о кофе
cur.execute('SELECT * FROM coffee')
coffee_data = cur.fetchall()

# Вывод информации о кофе
for coffee in coffee_data:
    print(f'ID: {coffee[0]}')
    print(f'Название сорта: {coffee[1]}')
    print(f'Степень обжарки: {coffee[2]}')
    print(f'Молотый/в зернах: {coffee[3]}')
    print(f'Описание вкуса: {coffee[4]}')
    print(f'Цена: {coffee[5]}')
    print(f'Объем упаковки: {coffee[6]}')

# Закрытие соединения с базой данных
conn.close()