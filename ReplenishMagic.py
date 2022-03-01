'''
Replenish character magic by resetting
Later on add in magic runes/stones or some other object to replenish
'''

import sqlite3 as sl
from contextlib import closing
import GlobalVariablesUpdate
import GlobalVariablesConfig

def ReplenishMagic():

    conn = sl.connect('InvenMania.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT magic FROM Characters where charactername = "' + GlobalVariablesConfig.charactername + '"')
        data = cursor.fetchall()
        GlobalVariablesConfig.charactermagic = str(list(data))[2:-3]


    with closing(sl.connect('InvenMania.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()