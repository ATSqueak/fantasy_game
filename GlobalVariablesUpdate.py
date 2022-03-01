'''
Update global variables
'''

import sqlite3 as sl
from contextlib import closing
import GlobalVariablesConfig

def UpdateHealth():
    conn = sl.connect('InvenMania.db')

    charName = GlobalVariablesConfig.charactername

    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT health FROM Characters where charactername = "' + GlobalVariablesConfig.charactername + '"')
        data = cursor.fetchall()
        GlobalVariablesConfig.characterhealth = str(list(data))[2:-3]
        cursor.execute('SELECT magic FROM Characters where charactername = "' + GlobalVariablesConfig.charactername + '"')
        data = cursor.fetchall()
        GlobalVariablesConfig.charactermagic = str(list(data))[2:-3]


    with closing(sl.connect('InvenMania.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
