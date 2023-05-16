# Exercise 1 : Restaurant Menu Manager
# Instructions
# Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete an item.

# PART 1
# In this exercise we will use PostgreSQL and Python. Create a new database and a new table in pgAdmin (or in psql). Read the instructions below before creating the new table

# Create a new class called MenuItem, the attributes should be the name and price of each item.

# Create several methods (save, delete, update) these methods will allow a user to save, delete and update items from the database.

# Within the MenuItem class create a method called all which will return a list of all our MenuItem objects.

# Create another method called get_by_name that will return a single MenuItem object depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.

# Codebox:

# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item2 = MenuItem.get_by_name('Beef Stew')
# items = MenuItem.all()

# Part 2
# Create a file called menu_editor.py , which will have the following functions:
# load_manager()- this function should create a new MenuItem instance.

# show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to choose an item. Call the appropriate function that matches the user’s input.

# add_item_to_menu() - this will ask the user to input the item’s name and price. It will not interact with the menu itself, but simply call the appropriate function from the MenuItem object.
# If the item was added successfully print a message which states: item was added successfully.

# remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. The function should not interact with the menu itself, but simply call the appropriate function from the MenuItem object.
# If the item was deleted successfully – print a message to let the user know this was completed.
# If not – print a message which states that there was an error.

# show_restaurant_menu() - print the restaurant’s menu.

# When the user chooses to exit the program, display the restaurant menu and exit the program.

# Here’s an example of the menu shown to the user:


