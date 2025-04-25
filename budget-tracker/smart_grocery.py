grocery_list = {}
budget = 0.0

def set_budget():
    global budget
    budget = float(input("Enter your total budget: "))
    print(f"Budget set to: {budget}")

def add_item():
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter the price per unit: "))
    grocery_list[item] = (quantity, price)
    print(f"Added {item}")

def view_list():
    print("Grocery List: ")
    for item, (qty, price) in grocery_list.items():
        print(f"- {item}: {qty} @ {price} = {qty * price}")

def calculate_total():
    total = sum(qty * price for qty, price in grocery_list.values())
    print(f"Total cost: {total}")
    print(f"Remaining budget: {budget - total}")
    if total > budget:
        print("Warning: You are over the budget!")

def remove_item():
    item = input("Enter item to remove: ")
    if item in grocery_list:
        del grocery_list[item]
        print(f"Removed {item}")
    else:
        print("Item not found!")

def apply_discount():
    item = input("Enter item to discount: ")
    if item in grocery_list:
        discount = float(input("Enter discount %: "))
        qty, price = grocery_list[item]
        discounted_price = round(price * (1 - discount/100), 2)
        grocery_list[item] = (qty, discounted_price)
        print(f"New price for {item}: {discounted_price}")
    else:
        print("Item not on list")

def main():
    print("Welcome to the Smart Grocery List App")
    set_budget()
    while True:
        print("""
            1. Add item
            2. Remove Item
            3. View List
            4. Calculate total
            5. Apply discount
            6. Exit
            """)
        choice = input("Your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            calculate_total()
        elif choice == "5":
            apply_discount()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!!")

main()
