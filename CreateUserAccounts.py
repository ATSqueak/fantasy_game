import sqlite3 as sl

conn = sl.connect('InvenMania.db')

with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS UserAccount (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        firstname TEXT,
        lastname TEXT,
        password TEXT,
        UNIQUE(id,firstname,lastname)
        );
    """)

sql = 'INSERT OR IGNORE INTO UserAccount (id,firstname,lastname,password) VALUES (?,?,?,?)'
data = [
    (1,'Rayyan','Taha','seep'),
    (2,'Advait','Abhyankar','reep'),
    (3,'Crisps','Saline','veep')
]
with conn:
    conn.executemany(sql,data)

with conn:
    data = conn.execute('SELECT * FROM UserAccount')
    for row in data:
        print(data)