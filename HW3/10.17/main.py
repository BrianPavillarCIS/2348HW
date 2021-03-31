# Name: Brian Pavillar
# ID: 1863509

class ItemToPurchase:
    def __init__(self, item_name = "None", item_price = 0.0, item_quantity = 0):
        self.name = item_name
        self.price = item_price
        self.quantity = item_quantity

    def print_item_cost(self):
        cost = self.price * self.quantity
        return cost


class ItemToPurchase:
    def __init__(self, item_name="None", item_price=0.0, item_quantity=0):
        self.name = item_name
        self.price = item_price
        self.quantity = item_quantity

    def print_item_cost(self):
        cost = self.price * self.quantity
        return cost

if __name__ == "__main__":

    print("Item 1")
    item_name = str(input("Enter the item name:\n"))
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n\n"))

    items1 = ItemToPurchase(item_name, item_price, item_quantity)

    print("Item 2")
    item_name = str(input("Enter the item name:\n"))
    item_price = float(input("Enter the item price:\n"))
    item_quantity = int(input("Enter the item quantity:\n\n"))

    items2 = ItemToPurchase(item_name, item_price, item_quantity)

    # Zybooks wants me to format it without floats. A normal pricing system wouldn't be like this, so this threw me a bit off.
    print("TOTAL COST")
    print(items1.name, items1.quantity, "@ ${:.0f} = ${:.0f}".format(items1.price, items1.print_item_cost()))
    print(items2.name, items2.quantity, "@ ${:.0f} = ${:.0f}\n".format(items2.price, items2.print_item_cost()))

    total = items1.print_item_cost() + items2.print_item_cost()
    print("Total: ${:.0f}".format(total))