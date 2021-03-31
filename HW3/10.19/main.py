# Name: Brian Pavillar
# ID: 1863509

class ItemToPurchase:
    def __init__(self, item_name = "None", item_price = 0.0, item_quantity = 0, item_description = "None"):
        self.name = item_name
        self.price = item_price
        self.quantity = item_quantity
        self.description = item_description

    def print_item_cost(self):
        cost = self.price * self.quantity
        return cost

    def print_item_description(self):
        print("{}: {}".format(self.name, self.description))


class ShoppingCart:
    def __init__(self, customer_name="None", current_date = "January 1, 2016", cart_items = []):
        self.name = customer_name
        self.date = current_date
        self.items = cart_items

    def add_item(self):
        self.items.append(ItemToPurchase)

    def remove_item(self):
        self.items.pop(ItemToPurchase)

    # Incomplete "modify" function
    # def modify_item(self):
        # if ItemToPurchase == True:
            # self.items."modify"(ItemToPurchase)
        # else:
            # print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        for stuff in self.items:
            return self.items.count(stuff)

    def get_cost_of_cart(self):
        total = self.items * ItemToPurchase.print_item_cost(self)
        print("Total:", total)

    def print_description(self):


if __name__ == "__main__":

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    ShoppingCart(customer_name, current_date)

    def print_menu():
        user_input = input("MENU \n a - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n\nChoose an option:")
            if user_input == "a":
                ShoppingCart.add_item()
            elif user_input == "r":
                ShoppingCart.remove_item()
            # Incomplete "modify" function
            # elif user_input == "c":
                # ShoppingCart.modify_item()
            elif user_input == "i":
                ShoppingCart.printdescription()

    print_menu(ShoppingCart)