'''
Login Screen
Use DB user entry to allow entry to play
'''

import sqlite3 as sl
from contextlib import closing
import Introduction
import Register
import GlobalVariablesConfig
import sys

def logIn():
    print()
    username = input('Enter your login username:-  ')
    print()
    print('Checking....')
    #print(username)

    conn = sl.connect('InvenMania.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM UserAccount')
    result = cursor.fetchall()

    #convert tuple output to a list and then a string and remove the brackets and inverted commas returned by the SQLITE query
    result = [str(list(row))[2:-2] for row in result]

    matched = False

    if username in result:
        print('Matched!  Hello ' + username)
        GlobalVariablesConfig.username = username
        matched = True
    else:
        print('User account not found')
        matched = False

    if matched == True:
        Introduction.intro()
    elif matched == False:
        Register.register()
        sys.exit(0)

    with closing(sl.connect('InvenMania.db')) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
            #print(rows)


''' 
'''