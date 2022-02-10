'''
Introductory text pulled in from text files

# From StackOverflow.. to use a function from a file in a different directory
#import sys
#sys.path.append('/Users/arif/PycharmProjects/TestArea/FantasyGame/ChooseCharacter/')

'''


def intro():
    with open('/Users/arif/PycharmProjects/TestArea/FantasyGame/Text/' + 'Inroduction.txt','r') as textFile:
        for line in textFile:
           print(line)

    import ChooseCharacter as choose
    choose.ChoosePlayerCharacter()






