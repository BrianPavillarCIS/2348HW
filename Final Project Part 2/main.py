# Name: Brian Pavillar
# ID: 1863509

# import modules and global variables
import datetime
import csv

inventory = dict()
manufacturers = []
itemtypes = []

# class constructors as used in Part 1
class InventoryItem:
    def __init__(self):
        self.itemId = -1
        self.manufacturerName = ""
        self.itemType = ""
        self.damaged = True
        self.price = -1.0
        self.serviceDate = datetime.date(1970, 1, 1)

    def __init__(self, itemId, manuName, itemType, damaged, price=-1.0, serviceDate=datetime.date(1970, 1, 1)):
        self.itemId = itemId
        self.manufacturerName = manuName
        self.itemType = itemType
        self.damaged = damaged
        self.price = price
        self.serviceDate = serviceDate

    # leadin: prepend the output string for the output requirements of a.ii versus a.iii
    def productstring(self, leadin):
        print(leadin + self.manufacturerName + " " + self.itemType + ", price: " + str(self.price))

# key reference as used in part 1
def pricesort(e):
    return e.price

# main() function from part 1
def prepareinventory():
    # prepare the inventory dict
    # some pre-processing lists to make input validation during querying easy
    with open('ManufacturerList.csv', newline='') as manufile:
        manureader = csv.reader(manufile, delimiter=',')
        for row in manureader:
            # in order by id, manufacturer, product type, and if damaged
            newitem = InventoryItem(int(row[0]), str(row[1]).strip(), str(row[2]).strip(), str(row[3]).strip() == 'damaged')
            inventory[int(row[0])] = newitem
            # populate the lists with manufacturer and item types
            if row[1] not in manufacturers:
                manufacturers.append(newitem.manufacturerName)
            if row[2] not in itemtypes:
                itemtypes.append(newitem.itemType)

    # add price to each inventory entry by key
    with open('PriceList.csv') as pricefile:
        pricereader = csv.reader(pricefile, delimiter=',')
        for row in pricereader:
            inventory[int(row[0])].price = float(row[1])

    # add service date to each inventory entry by key
    # using datetime so it's easier to do comparisons during queries
    with open('ServiceDatesList.csv') as datefile:
        datereader = csv.reader(datefile, delimiter=',')
        for row in datereader:
            dateparts = str(row[1]).split('/')
            inputdate = datetime.date(int(dateparts[2]), int(dateparts[0]), int(dateparts[1]))
            inventory[int(row[0])].serviceDate = inputdate

def executequery(querystr):
    # split string into different parameters
    queryfeatures = querystr.split(' ')
    manufacturer = None
    itemtype = None

    # a.iv: if quit is true, exit
    if querystr.strip() == "q":
        quit()

    # a.i: if true, we found a duplicate of a given element type e.g. "Apple Dell tower"
    # from directions, we return no such inventory
    excessparameterfound = False
    
    # We can't get a pair from a single element
    if len(queryfeatures) < 2:
        print("No such item in inventory")
        return
    else:
        # loop through the query elements and extract a manu and a itemtype
        # flags for repeated words, excess words, and if two different manu/item types
        for feature in queryfeatures:
            if manufacturer is not None and feature in manufacturers:
                excessparameterfound = True
            elif feature in manufacturers:
                manufacturer = feature
            if itemtype is not None and feature in itemtypes:
                excessparameterfound = True
            elif feature in itemtypes:
                itemtype = feature
    if manufacturer is None or itemtype is None or excessparameterfound:
        print("No such item in inventory")
        return

    # a.ii: Filter inventory by the manufacturer/itemtype pair and etc 
    today = datetime.date.today()
    candidates = []
    alternates = []
    for key in inventory.keys():
        item = inventory[key]
        # a.ii: Filtering according to parameters (manufacturer, item type, etc)
        if item.manufacturerName == manufacturer and item.itemType == itemtype and item.serviceDate > today and item.damaged is False:
            candidates.append(item)
        # a.iii: If it's the same item type and otherwise valid, we include it in alternatives
        elif item.itemType == itemtype and item.serviceDate > today and item.damaged is False:
            alternates.append(item)
    if len(candidates) == 0:
        print("No such item in inventory")
        return

    # sort by price descending, grab candidates[0] and [1] for the search output
    candidates.sort(key=pricesort,reverse=True)
    # a.ii: Print best match
    finalCandidate = candidates[0]
    finalCandidate.productstring("Your item is: ")
    # a.iii: If we have one alternative that's valid, give it
    if len(alternates) == 1:
        alternates[0].productstring("You may also consider: ")
    # a.iii: If multiple alternatives, decide which alternative is closest in price using absolute value of the difference
    if len(alternates) > 1:
        bestdifference = 99999
        bestalternative = None
        for i in range(len(alternates)):
            # abs gets the absolute value of difference
            difference = abs(alternates[i].price - finalCandidate.price)
            # comparing price values
            if difference < bestdifference:
                bestdifference = difference
                bestalternative = alternates[i]
        bestalternative.productstring("You may also consider: ")

if __name__ == '__main__':
    # function call
    prepareinventory()
    # loops until 'q' is called
    while True:
        query = (str(input("Give input:")))
        executequery(query)
