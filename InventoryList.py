import sqlite3 as sl

conn = sl.connect('InvenMania.db')

with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS InventoryList (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        item,
        UNIQUE(id,item)
        );
    """)

sql = 'INSERT OR IGNORE INTO InventoryList (id,item) VALUES (?,?)'
data = [
    (1,'Axe'),
    (2,'Wooden Club'),
    (3,'Rope'),
    (4,'Flask'),
    (5,'Sword'),
    (6,'Bow'),
    (7,'Arrows'),
    (8,'Wand')
]
with conn:
    conn.executemany(sql,data)
