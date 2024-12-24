import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
        '''
        create table if not exists Url
        (id integer primary key,
        url text)
        ''')
connection.commit()
connection.close()

def get_original_url(id: int):
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row 
    cursor = connection.cursor()
    return cursor.execute('select url, id from "Url" where id = {id};'.format(id=id)).fetchone()

def insert_url(original_url: str):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(
        "Insert into Url(url) VALUES ('{original_url}');"
        .format(original_url=original_url))
    connection.commit()
    connection.close()
    return cursor.lastrowid.__str__()
