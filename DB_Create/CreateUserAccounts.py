
import sqlite3 as sl
from contextlib import closing

conn = sl.connect('../InvenMania.db')

with conn:
    conn.execute("""
        drop table UserAccount;
        """)

with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS UserAccount (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        firstname TEXT,
        lastname TEXT,
        password TEXT,
        UNIQUE(id,firstname,lastname)
        );
    """)

sql = 'INSERT OR IGNORE INTO UserAccount (id,username,firstname,lastname,password) VALUES (?,?,?,?,?)'
data = [
    (1,'Ray','Rayyan','Taha','seep'),
    (2,'ADT','Advait','Abhyankar','reep'),
    (3,'Coupon','Crisps','Saline','veep')
]
with conn:
    conn.executemany(sql,data)

'''
with conn:
    data = conn.execute('SELECT * FROM UserAccount')
    for row in data:
        print(data)
'''

with closing(sl.connect('InvenMania.db')) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()