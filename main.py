'''
main file
'''

import Login as lg
import GlobalVariablesConfig
import GlobalVariablesUpdate
import UpdateVillain
import ChapterOne
import ChapterTwo
import ChapterThree
import ChapterFour
import End
import Fight
import MagicFight
import ReplenishHealth
import ReplenishMagic

print('Start here...')
lg.logIn()
print('Your details are...')
print('User: ' + GlobalVariablesConfig.username)
print('Character: ' + GlobalVariablesConfig.charactername)
print('Health: ' + str(GlobalVariablesConfig.characterhealth))
print('Magic: ' + str(GlobalVariablesConfig.charactermagic))
print()
ChapterOne.ChapterOne()
GlobalVariablesConfig.villainname = 'Lesser'
UpdateVillain.UpdateVillain(GlobalVariablesConfig.villainname)
print('Villain: ' + GlobalVariablesConfig.villainname)
print('Villain Health: ' + str(GlobalVariablesConfig.villainhealth))
print('Villain Magic: ' + str(GlobalVariablesConfig.villainmagic))
print()
print('Prepare to fight...')
Fight.fight()
ReplenishHealth.ReplenishHealth()
ChapterTwo.ChapterTwo()
GlobalVariablesConfig.villainname = 'Sneak'
UpdateVillain.UpdateVillain(GlobalVariablesConfig.villainname)
print('Villain: ' + GlobalVariablesConfig.villainname)
print('Villain Health: ' + str(GlobalVariablesConfig.villainhealth))
print('Villain Magic: ' + str(GlobalVariablesConfig.villainmagic))
print()
print('Prepare to fight...')
Fight.fight()
ReplenishHealth.ReplenishHealth()
ChapterThree.ChapterThree()
GlobalVariablesConfig.villainname = 'Drobee'
UpdateVillain.UpdateVillain(GlobalVariablesConfig.villainname)
print('Villain: ' + GlobalVariablesConfig.villainname)
print('Villain Health: ' + str(GlobalVariablesConfig.villainhealth))
print('Villain Magic: ' + str(GlobalVariablesConfig.villainmagic))
print()
print('Prepare to fight...')
MagicFight.magicfight()
ReplenishMagic.ReplenishMagic()
ChapterFour.ChapterFour()
GlobalVariablesConfig.villainname = 'Clossal'
UpdateVillain.UpdateVillain(GlobalVariablesConfig.villainname)
print('Villain: ' + GlobalVariablesConfig.villainname)
print('Villain Health: ' + str(GlobalVariablesConfig.villainhealth))
print('Villain Magic: ' + str(GlobalVariablesConfig.villainmagic))
print()
print('Prepare to fight...')
MagicFight.magicfight()
ReplenishMagic.ReplenishMagic()
End.End()