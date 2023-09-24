stuff={'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
def displayInventory(inventory):
    print("Inventory:")
    total=0
    for k, v in inventory.items():
        print(str(v)," ",k)
        total=total+v
    print("Total number of items: ",total)
displayInventory(stuff)
def addToInventory(inventory,addedItems):
    for loot in addedItems:
        inventory.setdefault(loot,0)
        inventory[loot]+=1
    return inventory

inv={'gold coin':42,'rope':1}
dragon_loot=['gold coin','dagger','gold coin','gold coin','ruby']
inv=addToInventory(inv,dragon_loot)
displayInventory(inv)