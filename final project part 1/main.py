# Name: Brian Pavillar
# ID: 1863509


import datetime
import csv

inventory = dict()
manufacturers = []
itemtypes = []

class InventoryItem:
    # class constructors
    def __init__(self):
        self.itemId = -1
        self.manufacturerName = ""
        self.itemType = ""
        self.damaged = False
        self.price = -1.0
        self.serviceDate = datetime.date(1970, 1, 1)

    def __init__(self, itemId, manuName, itemType, damaged, price=-1.0, serviceDate=datetime.date(1970, 1, 1)):
        self.itemId = itemId
        self.manufacturerName = manuName
        self.itemType = itemType
        self.damaged = damaged
        self.price = price
        self.serviceDate = serviceDate

# these three are key references to make it easier to call the sort functions
def pricesort(e):
    return e.price

def datesort(e):
    return e.serviceDate

def manusort(e):
    return e.manufacturerName

def main():
    global inventory
    inventory = dict()
    with open('ManufacturerList.csv', newline='') as manufile:
        manureader = csv.reader(manufile, delimiter=',')
        for row in manureader:
            newitem = InventoryItem(int(row[0]), str(row[1]).strip(), str(row[2]).strip(), str(row[3]).strip() == 'damaged')
            inventory[int(row[0])] = newitem
            # fill in empty the empty manufacturers and item type lists
            if row[1] not in manufacturers:
                manufacturers.append(newitem.manufacturerName)
            if row[2] not in itemtypes:
                itemtypes.append(newitem.itemType)

    with open('PriceList.csv') as pricefile:
        pricereader = csv.reader(pricefile, delimiter=',')
        # adds price as a float into the list
        for row in pricereader:
            inventory[int(row[0])].price = float(row[1])

    with open('ServiceDatesList.csv') as datefile:
        datereader = csv.reader(datefile, delimiter=',')
        # adds service date into the list
        for row in datereader:
            dateparts = str(row[1]).split('/')
            inputdate = datetime.date(int(dateparts[2]), int(dateparts[0]), int(dateparts[1]))
            inventory[int(row[0])].serviceDate = inputdate

    return inventory

# these functions sort by price if damaged, past service date, etc.
def manubyname(inventory):
    inventorylist = []
    for key in inventory:
        inventorylist.append(inventory[key])
    inventorylist.sort(key=manusort)
    return inventorylist

def damagedpricesort(inventory):
    inventorylist = []
    for key in inventory.keys():
        if inventory[key].damaged is True:
            inventorylist.append(inventory[key])
    inventorylist.sort(key=pricesort)
    inventorylist.reverse()
    return inventorylist

def servicedatesort(inventory):
    inventorylist = []
    today = datetime.date.today()
    for key in inventory:
        if inventory[key].serviceDate < today:
            inventorylist.append(inventory[key])
    inventorylist.sort(key=datesort)
    return inventorylist

def itemtypesort(itemtype,inventory):
    inventorylist = []
    for key in inventory.keys():
        if inventory[key].itemType == itemtype:
            inventorylist.append(inventory[key])
    return inventorylist



if __name__ == '__main__':
    main()

    with open('FullInventory.csv', 'w+', newline='') as f:
        # sorts alphabetically by manufacturer
        manufacturersort = manubyname(inventory)
        fwrite = csv.writer(f)
        # fills in empty list by appending from InventoryItem parameters
        for row in manufacturersort:
            rowdata = []
            rowdata.append(row.manufacturerName)
            rowdata.append(row.itemType)
            rowdata.append(row.price)
            rowdata.append(row.serviceDate)
            rowdata.append(row.damaged)
            fwrite.writerow(rowdata)

    with open('DamagedInventory.csv', 'w+', newline='') as f:
        # filters if damaged and sorts by price
        damagedlist = damagedpricesort(inventory)
        fwrite = csv.writer(f)
        for row in damagedpricesort(inventory):
            rowdata = []
            rowdata.append(row.manufacturerName)
            rowdata.append(row.itemType)
            rowdata.append(row.price)
            rowdata.append(row.serviceDate)
            rowdata.append(row.damaged)
            fwrite.writerow(rowdata)

    with open('PastServiceDateInventory.csv', 'w+', newline='') as f:
        damagedlist = servicedatesort(inventory)
        fwrite = csv.writer(f)
        for row in servicedatesort(inventory):
            rowdata = []
            rowdata.append(row.manufacturerName)
            rowdata.append(row.itemType)
            rowdata.append(row.price)
            rowdata.append(row.serviceDate)
            rowdata.append(row.damaged)
            fwrite.writerow(rowdata)

    # using two parameters, itemtype(string) and inventory(list)
    for itemtype in itemtypes:
        inventorybyitemtype = itemtypesort(itemtype,inventory)
        # Creates new files by item type, naming each file by respective type
        with open (itemtype.capitalize() + "Inventory.csv", "w+", newline='') as f:
            fwrite = csv.writer(f)
            for row in itemtypesort(itemtype,inventory):
                rowdata = []
                rowdata.append(row.manufacturerName)
                rowdata.append(row.itemType)
                rowdata.append(row.price)
                rowdata.append(row.serviceDate)
                rowdata.append(row.damaged)
                fwrite.writerow(rowdata)