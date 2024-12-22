import sqlite3

def create_db():
    connection = sqlite3.connect('New_Year.db')
    cursor = connection.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS purchases (
id INTEGER PRIMARY KEY,
name TEXT UNIQUE,
item TEXT,
price INTEGER,
status TEXT

)
''')
    try:
        cursor.executemany('''
INSERT INTO purchases (name, item, price, status) VALUES (?, ?, ?, ?)
''', [
('Иван Иванович', 'Санки', 2000, 'куплен'),
('Ирина Сергеевна', 'Цветы', 3000, 'не куплен'),
('Алексей Петрович', 'Книга', 1500, 'не куплен'),
('Мария Владимировна', 'Игрушка', 1000, 'не куплен'),
('Ольга Павловна', 'Часы', 5000, 'куплен'),
('Сергей Николаевич', 'Кофеварка', 2500, 'куплен'),
('Екатерина Владимировна', 'Билеты', 3500, 'куплен'),
('Дмитрий Афанасьевич', 'Краски', 1200, 'не куплен'),
('Анна Сергеевна', 'Косметика', 2000, 'куплен'),
('Владимир Иванович', 'Спортивный инвентарь', 2700, 'не куплен')
])
    except sqlite3.IntegrityError:
        print("некоторые записи дублируются и не были добавлены.")

    connection.commit()
    connection.close()

def query_data():
    connection = sqlite3.connect('New_Year.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM purchases')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()

create_db()
query_data()

def initConnection():
    connection = sqlite3.connect('New_Year.db')
    return connection

def closeConnection(pconnection):
    if pconnection is not None:
        pconnection.commit()
        pconnection.close()
