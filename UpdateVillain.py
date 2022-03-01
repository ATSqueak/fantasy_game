'''
Update Villain details
'''

import sqlite3 as sl
from contextlib import closing
import GlobalVariablesUpdate
import GlobalVariablesConfig

def UpdateVillain(name):
    conn = sl.connect('InvenMania.db')

    with conn:
        cursor = conn.cursor()
        cursor.execute('SELECT villainname FROM Villains where villainname = "' + name + '"')
        data = cursor.fetchall()
        GlobalVariablesConfig.villainname = str(list(data))[3:-4]
        cursor.execute('SELECT health FROM Villains where villainname = "' + GlobalVariablesConfig.villainname + '"')
        data = cursor.fetchall()
        GlobalVariablesConfig.villainhealth = str(list(data))[2:-3]
        cursor.execute('SELECT magic FROM Villains where villainname = "' + GlobalVariablesConfig.villainname + '"')
        data = cursor.fetchall()
        GlobalVariablesConfig.villainmagic = str(list(data))[2:-3]


    with closing(sl.connect('InvenMania.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()