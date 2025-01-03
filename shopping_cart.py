def view_items(items, prices):
    print("\nAvailable Items:")
    for i in range(len(items)):
        print("Name:", items[i], "Price:", prices[i])

def add_to_cart(cart, items, prices):
    item_name = input("Enter the item name: ")
    if item_name not in items:
        print("Item not available.")
        return
    quantity = input("Enter the quantity: ")
    if not quantity.isdigit():
        print("Invalid quantity.")
        return
    quantity = int(quantity)
    price = prices[items.index(item_name)]
    cart.append([item_name, quantity, price, quantity * price])

def update_cart(cart):
    item_name = input("Which item to be updated: ")
    for entry in cart:
        if entry[0] == item_name:
            quantity = input("Enter the quantity to be updated: ")
            if not quantity.isdigit():
                print("Invalid quantity.")
                return
            quantity = int(quantity)
            entry[1] = quantity
            entry[3] = quantity * entry[2]
            print("Cart updated.")
            return
    print("Item not found in cart.")

def delete_from_cart(cart):
    item_name = input("Which item to be removed: ")
    for entry in cart:
        if entry[0] == item_name:
            cart.remove(entry)
            print("Item removed from cart.")
            return
    print("Item not found in cart.")

def print_bill(cart):
    print(cart)

def total_bill_print(cart):
    print("\nBill:")
    print("Name, Quantity, Price, Total")
    total_amount = 0
    for entry in cart:
        print(entry[0], entry[1], entry[2], entry[3], sep=", ")
        total_amount += entry[3]
    print("Total Amount of Bill", total_amount)

def main():
    items = ['Bread', 'Cookies', 'Butter', 'Cheese', 'Yoghurt']
    prices = [40, 80, 120, 180, 60]
    cart = []
    print (items)
    while True:
        print("Enter 1 for viewing the items")
        print("Enter 2 for adding the items in cart")
        print("Enter 3 for updating the items in cart")
        print("Enter 4 for deleting the items in cart")
        print("Enter 5 for printing bill")
        print("Enter 6 to exit")
        print("What you want to do?")

        choice = input("Enter the choice: ")
        if not choice.isdigit():
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue
        choice = int(choice)

        if choice == 1:
            view_items(items, prices)
            print("\n")
        elif choice == 2:
            add_to_cart(cart, items, prices)
            print("\n")
        elif choice == 3:
            update_cart(cart)
            print("\n")
        elif choice == 4:
            delete_from_cart(cart)
            print("\n")
        elif choice == 5:
            print_bill(cart)
        elif choice == 6:
            total_bill_print(cart)
            print("Exiting. Thank you for using the shopping cart!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
