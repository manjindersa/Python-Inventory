inventory = ["wooden staff", "wizard hat", "cloth shoes"]

print("\nThe Wizard Inventory program\n")
print("COMMAND MENU")
print("show - Show all items")
print("grab - Grab an item")
print("edit - Edit an item")
print("drop - Drop an item")
print("exit - Exit program")

while True:
    command = input("\nCommand: ").lower()

    if command == "show":
        if inventory:
            for i, item in enumerate(inventory, 1):
                print(f"{i}. {item}")
        else:
            print("No items in inventory.")

    elif command == "grab":
        if len(inventory) < 4:
            item_name = input("Name: ")
            inventory.append(item_name)
            print(f"{item_name} was added.")
        else:
            print("You can't carry any more items. Drop something first.")

    elif command == "edit":
        try:
            item_number = int(input("Number: "))
            if 1 <= item_number <= len(inventory):
                updated_name = input("Updated name: ")
                inventory[item_number - 1] = updated_name
                print(f"Item number {item_number} was updated.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif command == "drop":
        try:
            item_number = int(input("Number: "))
            if 1 <= item_number <= len(inventory):
                dropped_item = inventory.pop(item_number - 1)
                print(f"{dropped_item} was dropped.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif command == "exit":
        print("Bye!")
        break

    else:
        print("Invalid command. Please try again.")