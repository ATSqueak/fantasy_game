'''
Replenish hero health
At this time it will be simply reset

Later on an addition of health points and other additives will be provided
'''

import sqlite3 as sl
from contextlib import closing
import GlobalVariablesUpdate
import GlobalVariablesConfig

def ReplenishHealth():
    conn = sl.connect('InvenMania.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT health FROM Characters where charactername = "' + GlobalVariablesConfig.charactername + '"')
        data = cursor.fetchall()
        GlobalVariablesConfig.characterhealth = str(list(data))[2:-3]

    with closing(sl.connect('InvenMania.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
