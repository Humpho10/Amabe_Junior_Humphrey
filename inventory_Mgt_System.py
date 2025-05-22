inventory = {
    "orange": 15,
    "apple": 10,
    "banana": 20
}

while True:
    print("\nInventory Management System")
    print("1. View inventory")
    print("2. Add item")
    print("3. Update Item Quantity")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("Current inventory:")
        for item in inventory:
            print(item, ":", inventory[item])

    elif choice == "2":
        item = input("Enter item name: ").lower()
        if item in inventory:
            print("Item already exists")
        else:
            quantity = input("Enter quantity: ")
            inventory[item] = int(quantity)
            print(item, "added with quantity", quantity)

    elif choice == "3":
        item = input("Enter item name to update: ").lower()
        if item in inventory:
            quantity = input("Enter new quantity: ")
            inventory[item] = int(quantity)
            print(item, "updated to quantity", quantity)
        else:
            print("Item not found")

    elif choice == "4":
        print("Exiting program!!")
        break

    else:
        print("Invalid option. Please enter 1, 2, 3 or 4.")
