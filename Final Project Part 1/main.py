# Name: Brian Pavillar
# ID: 1863509

from csv import DictReader
import datetime

class item_list:

    # Get current date
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%x")

    def __init__(self, number, brand, type, price, service_date, status="undamaged"):
        self.number = number
        self.brand = brand
        self.type = type
        self.price = price
        self.service_date = service_date
        self.status = status

    # Should write all parameters as listed in item list into a new file
    def write_full_inv(self):
        with open("FullInventory.csv", "w") as f:
            f.write(self.number, self.brand, self.type, self.price, self.service_date, self.status)

    # Should write new files based on their item type (as laptop, phone, tower, or other)
    def write_by_type(self):
        # Sort function used to sort ID
        self.number.sort()
        # Checks if type matches with a certain parameter
        if self.type == "Laptop":
            with open("LaptopInventory.csv", "w") as f:
                f.write(self.number, self.brand, self.price, self.service_date, self.status)

        elif self.type == "Phone":
            with open("PhoneInventory.csv", "w") as f:
                f.write(self.number, self.brand, self.price, self.service_date, self.status)

        elif self.type == "Tower":
            with open("TowerInventory.csv", "w") as f:
                f.write(self.number, self.brand, self.price, self.service_date, self.status)

        else:
            with open("OtherInventory.csv", "w") as f:
                f.write(self.number, self.brand, self.price, self.service_date, self.status)

    # Determines if the current date is past the service date, then writes to a new file
    def write_by_past_date(self, current_date):
        if self.service_date < current_date:
            with open("PastServiceDateInventory.csv", "w") as f:
                f.write(self.number, self.brand, self.type, self.price, self.service_date, self.status)

    # Determines if the product is damaged or not
    def write_if_damaged(self):
        # Using "reverse" to sort from most expensive to least expensive
        self.price.reverse()
        if self.status == "damaged":
            with open("DamagedInventory.csv", "w") as f:
                f.write(self.number, self.brand, self.type, self.price, self.service_date)

# With statement opens this file
with open('ManufacturerList(1).csv', 'r') as f:
    # Use DictReader to convert information into dictionary
    reader = DictReader(f)
    # Dictionary Information gets contained within a list
    man_dict = list(reader)

# Repeat with statement
with open('PriceList(1).csv', 'r') as f:
    reader = DictReader(f)
    price_dict = list(reader)

with open('ServiceDatesList(1).csv', 'r') as f:
    reader = DictReader(f)
    dates_dict = list(reader)

# If ID's are the same, the dictionary should update man_dict by adding the price paramater to its respective ID.
if man_dict["ID"] == price_dict["ID"]:
    full_dict = man_dict.update(price_dict)

# If ID's are the same, the dictionary should update man_dict by adding the service date paramater to its respective ID.
if man_dict["ID"] == dates_dict["ID"]:
    full_dict.update(dates_dict)

# Calls the class function, no output in this file. It should be written into another file
item_list(full_dict)
