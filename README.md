# Python Inventory

## Description
The Python Inventory program is a simple command-line application that allows users to manage an inventory of items. Users can display all items, add new items, edit existing items, drop items, and exit the program through a command menu.

## Features
- **Show Items**: Display all items in the inventory.
- **Grab Item**: Add a new item to the inventory (up to a maximum of 4 items).
- **Edit Item**: Edit the name of an existing item in the inventory.
- **Drop Item**: Remove an item from the inventory.
- **Exit Program**: Exit the inventory management program.

## Usage
1. **Clone the Repository**: Clone the repository to your local machine.
    ```sh
    git clone https://github.com/manjindersa/Python-Inventory.git
    ```
2. **Navigate to the Directory**: Change to the directory containing the `Inventory.py` file.
    ```sh
    cd Python-Inventory
    ```
3. **Run the Program**: Execute the Python script.
    ```sh
    python Inventory.py
    ```
4. **Use the Command Menu**:
    - `show`: Display all items in the inventory.
    - `grab`: Add a new item to the inventory (max 4 items).
    - `edit`: Edit the name of an existing item.
    - `drop`: Remove an item from the inventory.
    - `exit`: Exit the program.

## Example
```
The Wizard Inventory program

COMMAND MENU
show - Show all items
grab - Grab an item
edit - Edit an item
drop - Drop an item
exit - Exit program

Command: show
1. wooden staff
2. wizard hat
3. cloth shoes

Command: grab
Name: magic wand
magic wand was added.

Command: edit
Number: 2
Updated name: enchanted hat
Item number 2 was updated.

Command: drop
Number: 1
wooden staff was dropped.

Command: exit
Bye!
```

## Code Structure

### Main Program
- **Inventory List**: Stores the items in the inventory.
- **Command Menu**: A loop that continuously prompts the user for commands and executes the corresponding actions.

### Commands
- **show**: Displays all items in the inventory.
- **grab**: Prompts for the name of a new item and adds it to the inventory if there are fewer than 4 items.
- **edit**: Prompts for an item number and a new name, then updates the specified item.
- **drop**: Prompts for an item number and removes the specified item from the inventory.
- **exit**: Exits the program.

## Author
- **Manjinder Singh**
- **GitHub**: [manjindersa](https://github.com/manjindersa)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, report issues, or suggest features by opening a pull request or issue on the [GitHub repository](https://github.com/manjindersa/Python-Inventory).
