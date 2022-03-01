'''
Inventory of current items in game
Not used in Version 1
'''
import pprint


def displayInventory(inventory):
    print('Your Inventory:')
    for k, v in inventory.items():
        print(k, v)


def displayInventoryTotalItem(inventory):
    print()
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item,
                             0)  # If the item in the list is not in the dictionary, then add it as a key to the dictionary - with a value of 0
        inventory[item] = inventory[item] + 1  # Increment the value of the key by 1

    return inventory


print('Fantasy Game Inventory List')
print()
currentInventory = {'rope': 2, "light torch": 3, "gold coin": 42, "dagger": 1, "sword": 1, "arrow": 12}
# displayInventory(currentInventory)
# displayInventoryTotalItem(currentInventory)
# pprint.pprint(currentInventory)
newInv = {"gold coin": 42, "rope": 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print('Before')
displayInventory(newInv)
newInv = addToInventory(newInv, dragonLoot)
print('After')
displayInventory(newInv)
