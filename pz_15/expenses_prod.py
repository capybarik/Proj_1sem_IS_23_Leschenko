#Вариант 15
#Приложение РАСХОДЫ ПО ВИДАМ ПРОДУКЦИИ для автоматизированного
#контроля затрат на производство продукции. БД должна содержать таблицу Расходы со
#следующей структурой записи: Дата, Код продукта, Наименование продукта, Расходы, Сумма.


import sqlite3 as sq
from data_prod import info_prod

with sq.connect('expenses_products.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS expenses (
        data DATE,
        prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        sum INTEGER NOT NULL
    )""")

#Ввод данных
with sq.connect('expenses_products.db') as con:
    cur = con.cursor()
    #cur.executemany("INSERT INTO expenses VALUES (?, ?, ?, ?, ?)", info_prod)


#3 запроса операции поиска
#with sq.connect('expenses_products.db') as con:
#    cur = con.cursor()
#    cur.execute("SELECT * FROM expenses WHERE sum BETWEEN 500 AND 2000")
#    result1 = cur.fetchall()
#    cur.execute("SELECT * FROM expenses WHERE type = 'Развлечения'")
#    result2 = cur.fetchall()
#    cur.execute("SELECT * FROM expenses WHERE type = 'Личные покупки' AND data = '2024-04-01'")
#    result3 = cur.fetchall()
#    print('Выборка, если сумма больше 500 и меньше 2000 >> ', result1)
#    print('Выборка, если категория расходов "Развлечения" >> ', result2)
#    print('Выборка, если категория расходов "Личные покупки" и дата 1 апреля 2024 >> ', result3)


#3 запроса операции редактирования
#with sq.connect('expenses_products.db') as con:
#    cur = con.cursor()
#    cur.execute("UPDATE expenses SET sum = 50 WHERE name LIKE 'Проездной'")
#    cur.execute("UPDATE expenses SET data = '2024-04-04' WHERE type LIKE 'Еда'")
#    cur.execute("UPDATE expenses SET type = 'Техника', sum = 100000 WHERE data = '2024-04-01'")


#3 запроса операции удаления
with sq.connect('expenses_products.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM expenses WHERE prod_id = 9")
    cur.execute("DELETE FROM expenses WHERE sum < 500")
    cur.execute("DELETE FROM expenses WHERE data = '2024-03-30' AND name LIKE 'Батут'")



