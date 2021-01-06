stuff={'rope ':1  , 'torch':6 , 'gold coin':42 , 'dagger':1 , 'arrow': 12}
items_list ={'gold coin', 3 , 'ruby',1 , 'dagger', 2}
def addToInventory(inventory , addedItems):
    items_total = 0
    it=iter(addedItems)
    res_dct=dict(zip(it , it))
    return res_dct
    if addedItems in inventory :
        inventory.update(addedItems)
        for k,v in inventory.items():
            items_total += v
    if addedItems not in inventory:
        for k,v in inventory.items():
            inventory.setdefault(addedItems)
            print(str(v)+ '  ' + k)
            items_total += v
        print("Total number of items: "+ str(items_total))
addToInventory(stuff,items_list)
     
