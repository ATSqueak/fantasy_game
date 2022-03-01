'''
Opponents or Villains:
Sneak - Thief
Lesser - Fighter
Clossal - Dragon
Drobee - Magician
'''


import sqlite3 as sl
from contextlib import closing

conn = sl.connect('../InvenMania.db')

with conn:
    conn.execute("""
        drop table Villains;
        """)

with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Villains (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        villainname TEXT,
        species TEXT,
        health INTEGER,
        magic INTEGER,
        UNIQUE(id,villainname,species)
        );
    """)

sql = 'INSERT OR IGNORE INTO Villains (id,villainname,species,health,magic) VALUES (?,?,?,?,?)'
data = [
    (1,'Sneak','Thief',20,10),
    (2,'Lesser','Fighter',20,10),
    (3,'Clossal','Dragon',20,50),
    (4,'Drobee','Magician',20,50)
]
with conn:
    conn.executemany(sql,data)

with conn:
    data = conn.execute('SELECT * FROM Villains')
    for row in data:
        print(data)

with closing(sl.connect('InvenMania.db')) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()