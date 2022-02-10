'''
Choose which character you want to be


    (1,'Tusk','Dwarf'),
    (2,'Ethrel','Elf'),
    (3,'Savour','Wizard'),
    (4,'Steep','Warrior')
'''

def ChoosePlayerCharacter():
    character_list = {1: "Tusk", 2: "Ethrel", 3: "Savour", 4: "Steep"}

    print('1. Tusk - A Dwarf')
    print('2. Ethrel - An Elf')
    print('3. Savour - A Wizard')
    print('4. Steep - A Warrior')

    character = input('Choose your character from the list (input the number): ')
    # print(character)
    if character == "1":
        print("You have chosen Tusk a hardy Dwarf!")
    elif character == "2":
        print("You have chosen Ethrel a graceful Elf!")
    elif character == "3":
        print("You have chosen Savour a cunning Wizard!")
    elif character == "4":
        print("You have chosen Steep a powerful Warrior!")
    else:
        print('You must enter a corresponding number for the character you want.')
    # print(type(character))
    return character



