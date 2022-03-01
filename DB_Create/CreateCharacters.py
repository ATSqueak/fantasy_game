'''
Characters:
Tusk - Dwarf
Ethrel - Elf
Savour - Wizard
Steep - Warrior
'''

import sqlite3 as sl
from contextlib import closing

conn = sl.connect('../InvenMania.db')

with conn:
    conn.execute("""
        drop table Characters;
        """)

with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS Characters (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        charactername TEXT,
        species TEXT,
        health INTEGER,
        magic INTEGER,
        UNIQUE(id,charactername,species)
        );
    """)

sql = 'INSERT OR IGNORE INTO Characters (id,charactername,species,health,magic) VALUES (?,?,?,?,?)'
data = [
    (1,'Tusk','Dwarf',20,10),
    (2,'Ethrel','Elf',20,20),
    (3,'Savour','Wizard',20,50),
    (4,'Steep','Warrior',20,10)
]
with conn:
    conn.executemany(sql,data)

with conn:
    data = conn.execute('SELECT * FROM Characters')
    for row in data:
        print(data)

with closing(sl.connect('InvenMania.db')) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()