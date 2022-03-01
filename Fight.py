'''
Fight with a villain
Uses a random generator to match a dice roll against the two combatants
The highest will win that blow
'''

#character rolls die
#villain rolls die
#highest number wins
#loser will lose one unit of energy...

import random
import GlobalVariablesUpdate
import GlobalVariablesConfig
import sys

def fight():

    print('This is a battle between ' + GlobalVariablesConfig.charactername + ' and ' + GlobalVariablesConfig.villainname)
    print('Each character will roll and equal numbers means you win the round.')
    print('Each time you lose a round then you will have 2 points removed from your health')
    print('If you health is reduced to zero you will unfortunately die.')

    keep_going = True
    while keep_going:
        # "Roll" random dice
        heroDice = random.randint(1, 6)
        villainDice = random.randint(1,6)
        #print(type(GlobalVariablesConfig.villainhealth))
        #print(type(GlobalVariablesConfig.characterhealth))
        if heroDice >= villainDice:
            print('You rolled: ' + str(heroDice) + ' and the enemy rolled: ' + str(villainDice))
            print('You won this round')
            GlobalVariablesConfig.villainhealth = int(GlobalVariablesConfig.villainhealth) - 2
            print('Hero ' + str(GlobalVariablesConfig.characterhealth))
            print('Villain ' + str(GlobalVariablesConfig.villainhealth))
            if GlobalVariablesConfig.villainhealth <= 0:
                print('You have defeated ' + GlobalVariablesConfig.villainname)
                break
        else:
            print('You rolled: ' + str(heroDice) + ' and the enemy rolled: ' + str(villainDice))
            print('You lost this round')
            GlobalVariablesConfig.characterhealth = int(GlobalVariablesConfig.characterhealth) - 2
            print('Hero ' + str(GlobalVariablesConfig.characterhealth))
            print('Villain ' + str(GlobalVariablesConfig.villainhealth))
            if GlobalVariablesConfig.characterhealth <= 0:
                print('You have been defeated by ' + GlobalVariablesConfig.villainname)
                print('Better luck next time...')
                sys.exit(0)
        if int(GlobalVariablesConfig.villainhealth) or int(GlobalVariablesConfig.characterhealth) <= 0:
            keep_going = False
        else:
            keep_going = True
        keep_going = True
        #keep_going = input("Hit [Enter] to keep going, any key to exit: ") == ""
