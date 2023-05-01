# 1. Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# 2. Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# 3. Now that we have a list of fruits, ask the user to input a name of any fruit.
# - If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# - If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

import re

run = True

while run:
    favorite_fruits = input("Enter your favorite fruit(s) (separate with a space in case of multiple inputs): ")

    res = bool(re.match('[a-zA-Z\s]+$', favorite_fruits))

    if res:
        input_list = favorite_fruits.split(" ")

        input_list = [fruit.lower() for fruit in input_list]

        print(input_list)

        favorite_pick = input("Enter the name of your favorite fruit: ")

        if favorite_pick.isalpha():
            if favorite_pick.lower() in input_list:
                print("You chose one of your favorite fruits! Enjoy!")
            else:
                print("You chose a new fruit. I hope you enjoy")
        else:
            print("Wrong input.")

        run = False
    else:
        print("Wrong input. Please try again.")
