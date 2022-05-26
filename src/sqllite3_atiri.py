
import sqlite3
'''
try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")





'''

#try:
#    sqlite_connection = sqlite3.connect('sqlite_python.db')
#    sqlite_create_table_query = '''CREATE TABLE sql_atiri (
#                                python TEXT
#                                );'''
#
#    cursor = sqlite_connection.cursor()
#    print("База данных подключена к SQLite")
#    cursor.execute(sqlite_create_table_query)
#    sqlite_connection.commit()
#    print("Таблица SQLite создана")
#
#    cursor.close()
#
#except sqlite3.Error as error:
#    print("Ошибка при подключении к sqlite", error)
#finally:
#    if (sqlite_connection):
#        sqlite_connection.close()
#        print("Соединение с SQLite закрыто")
#
#
#

#try:
#    sqlite_connection = sqlite3.connect('sqlite_python.db')
#    cursor = sqlite_connection.cursor()
#    print("Подключен к SQLite")
#
#    sqlite_insert_query = """INSERT INTO sql_atiri
#                          (python)
#                          VALUES
#                          ('https://pythonworld/');"""
#    count = cursor.execute(sqlite_insert_query)
#    sqlite_connection.commit()
#    print("Запись успешно вставлена в таблицу sqlitedb_developers ", cursor.rowcount)
#    cursor.close()
#
#except sqlite3.Error as error:
#    print("Ошибка при работе с SQLite", error)
#finally:
#    if sqlite_connection:
#        sqlite_connection.close()
#        print("Соединение с SQLite закрыто")


def insert_multiple_records(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_query = """INSERT INTO sql_atiri
                                 (python)
                                 VALUES (?);"""

        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()
        print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def fetch():
    with sqlite3.connect('sqlite_python.db') as db:
        cursor=db.cursor()
        cursor.execute('SELECT python FROM sql_atiri')
        product=cursor.fetchall()
        product=str(product)
    return product

#records_to_insert = [('https://python.org',),
#                     ('https://pythonru.com',),
#                     ('https://habr.com',),]
