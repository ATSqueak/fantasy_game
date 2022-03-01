'''
Fight with a villain using magic
Uses a random generator to match a dice roll against the two combatants
The highest will win that blow
'''

import random
import GlobalVariablesUpdate
import GlobalVariablesConfig
import sys

def magicfight():

    print('This is a magical battle between ' + GlobalVariablesConfig.charactername + ' and ' + GlobalVariablesConfig.villainname)
    print('Each character will roll and equal numbers means you win the round.')
    print('Each time you lose a round then you will have 2 points removed from your magic')
    print('If you magic is reduced to zero you will unfortunately die.')

    keep_going = True
    while keep_going:
        # "Roll" random dice
        heroDice = random.randint(1, 6)
        villainDice = random.randint(1,6)
        if heroDice >= villainDice:
            print('You rolled: ' + str(heroDice) + ' and the enemy rolled: ' + str(villainDice))
            print('You won this round')
            GlobalVariablesConfig.villainmagic = int(GlobalVariablesConfig.villainmagic) - 2
            print('Hero ' + str(GlobalVariablesConfig.charactermagic))
            print('Villain ' + str(GlobalVariablesConfig.villainmagic))
            if GlobalVariablesConfig.villainmagic <= 0:
                print('You have defeated ' + GlobalVariablesConfig.villainname)
                break
        else:
            print('You rolled: ' + str(heroDice) + ' and the enemy rolled: ' + str(villainDice))
            print('You lost this round')
            GlobalVariablesConfig.charactermagic = int(GlobalVariablesConfig.charactermagic) - 2
            print('Hero ' + str(GlobalVariablesConfig.charactermagic))
            print('Villain ' + str(GlobalVariablesConfig.villainmagic))
            if GlobalVariablesConfig.charactermagic <= 0:
                print('You have been defeated by ' + GlobalVariablesConfig.villainname)
                print('Better luck next time...')
                sys.exit(0)
        if int(GlobalVariablesConfig.villainmagic) or int(GlobalVariablesConfig.charactermagic) <= 0:
            keep_going = False
        else:
            keep_going = True
        keep_going = True