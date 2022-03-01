'''
Save to DB character chosen by player with user account

'''
import sqlite3 as sl
from contextlib import closing


def SavePlayerCharacter(user, character):
    '''
    save the choice of character to DB against the username
    DB Table UserCharacter
    '''

    conn = sl.connect('../InvenMania.db')

    sql = 'INSERT OR IGNORE INTO UserCharacter (id,username,charactername, userID) VALUES (?,?,?,?)'
    #id = 1
    #username = whatever enetered  need to capture this in a global variable?
    #charatername = whatever is chosen in Intro/Login
    #userID = map back to UserAccount table
    data = []
'''
    data = [
        (1, 'Ray', 'Rayyan', 'Taha', 'seep'),
        (2, 'ADT', 'Advait', 'Abhyankar', 'reep'),
        (3, 'Coupon', 'Crisps', 'Saline', 'veep')
    ]
'''
    with conn:
        conn.executemany(sql, data)

    with conn:
        data = conn.execute('SELECT * FROM UserCharacter')
        for row in data:
            print(data)

    with closing(sl.connect('InvenMania.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()