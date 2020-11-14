# fantasy game inventory
# write function called display inventory that shows just what is held
# in an inventory dictionary datat structure

TOT_CAP = 10
stuff = { 'rope':0, 'torch':0, 'gold coin':42, 'dagger':1, 'arrow':0 }

def displayInventory( inventory ):
    print( "Inventory:" )
    item_total = 0
    for item, amount in inventory.items():
        print( str(amount) + ' ' + item )
        item_total += 1
    # print the total bag size and curr amount of items
    print( "Current Capacity: " + str( item_total ))
    print( "Total Capacity: " + str( TOT_CAP ))

displayInventory( stuff ) 
