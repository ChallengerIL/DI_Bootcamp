from exercisesxp import MenuItem


def load_manager(name, price):
    return MenuItem(name, price)


def show_user_menu():
    menu_options = {
        "a": "Add an item",
        "d": "Delete an item",
        "v": "View the menu",
        "x": "Exit",
    }

    menu_actions = {
        "Add an item": add_item_to_menu,
        "Delete an item": remove_item_from_menu,
        "View the menu": show_restaurant_menu,
        "Exit": quit,
    }

    print(" "*4 + "MENU")
    {print(f"({key}) {value}") for key, value in menu_options.items()}

    try:
        users_choice = input(" : ")[0].lower()
    except ValueError:
        print("Only letters are allowed")
    else:
        if users_choice in menu_options.keys():
            action = menu_options[users_choice]

            if users_choice == 'x':
                show_restaurant_menu()

            menu_actions[action]()
        else:
            print("Wrong input...")


def add_item_to_menu():
    item_name = input("Adding an item. Please enter the item's name: ")
    try:
        item_price = int(input("Adding an item. Please enter the item's price: "))
    except ValueError:
        print("Only integers are allowed")
    else:
        new_item = load_manager(item_name, item_price)
        result = new_item.save()

        if result:
            print("item was added successfully")


def remove_item_from_menu():
    item_name = input("Removing an item. Please enter the item's name: ")
    item = MenuItem.get_by_name(item_name)

    if not item:
        return print("Item not found")

    if item.delete():
        print("Item was deleted successfully")


def show_restaurant_menu():
    print([item.name for item in MenuItem.all()])


if __name__ == "__main__":
    while True:
        show_user_menu()
