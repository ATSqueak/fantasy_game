'''
Whatever character the user creates will be assigned to their account
to persist every time they want to play

'''


import sqlite3 as sl
from contextlib import closing

conn = sl.connect('../InvenMania.db')

with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS UserCharacter (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        charactername TEXT,
        userID,
        UNIQUE(id,username, charactername)
        );
    """)


with conn:
    data = conn.execute('SELECT * FROM UserCharacter')
    for row in data:
        print(data)

with closing(sl.connect('InvenMania.db')) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()