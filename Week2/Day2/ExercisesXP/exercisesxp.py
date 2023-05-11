# EXERCISE 1
# 1. Create a set called my_fav_numbers with all your favorites numbers.
# 2. Add two new numbers to the set.
# 3. Remove the last number.
# 4. Create a set called friend_fav_numbers with your friend’s favorites numbers.
# 5. Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

import random

START = 0
END = 100

my_fav_numbers = {3, 7}


def set_extender(start, end, my_set):
    new_number = random.randint(start, end)
    my_set.add(new_number)


run = 2

print(f"My initial fav numbers: {my_fav_numbers}")

for _ in range(run):
    set_extender(START, END, my_fav_numbers)

print(f"My fav numbers after adding two more numbers: {my_fav_numbers}")

last_element = list(my_fav_numbers)[-1]

my_fav_numbers.remove(last_element)

print(f"My fav numbers after removing the last number: {my_fav_numbers}")

friend_fav_numbers = set()

for _ in range(5):
    set_extender(START, END, friend_fav_numbers)

print(f"My friend's fav numbers: {friend_fav_numbers}")

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(f"Our fav numbers: {our_fav_numbers}")


# EXERCISE 2
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# The answer is No because tuples are immutable.


# EXERCISE 3
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# 1. Remove “Banana” from the list.
# 2. Remove “Blueberries” from the list.
# 3. Add “Kiwi” to the end of the list.
# 4. Add “Apples” to the beginning of the list.
# 5. Count how many apples are in the basket.
# 6. Empty the basket.
# 7. Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.pop(0)
basket.pop(-1)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(f"There are this many apples in the basket: {basket.count('Apples')}")
basket.clear()
print(basket)


# EXERCISE 4
# 1. Recap – What is a float? What is the difference between an integer and a float?
# 2. Can you think of another way to generate a sequence of floats?
# 3. Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# 1. Integers are numbers without decimal points. Floats are numbers with decimal points.

import numpy as np

# Numpy solution
first_sequence = list(np.arange(1.5, 5.5, .5))
print(first_sequence)

# List solution
second_sequence = [x / 2 for x in range(3, 11)]
print(second_sequence)


# EXERCISE 5
# 1. Use a for loop to print all numbers from 1 to 20, inclusive.
# 2. Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# 1
for i in range(1, 21):
    print(i)

print("\n")

# 2
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# EXERCISE 6
# 1. Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

target_name = "Iurii"
run = True

while run:
    user_name = input("What is your name?\n").title()
    
    if user_name == target_name:
        run = False


# EXERCISE 7
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


# EXERCISE 8
# 1. Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# 2. As they enter each topping, print a message saying you’ll add that topping to their pizza.
# 3. Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

PIZZA_PRICE = 10

run = True
toppings = list()

while run:
    topping = input("What toppings would you like?\n")
    if topping == "quit":
        run = False
    else:
        print(f"We will add {topping} to your pizza.")
        toppings.append(topping)

print(f"Your pizza toppings will include: {', '.join(toppings)}")

toppings_price = len(toppings) * 2.5

print(f"Your total pizza price is ${PIZZA_PRICE + toppings_price}")


# EXERCISE 9
# 1. A movie theater charges different ticket prices depending on a person’s age.
# - if a person is under the age of 3, the ticket is free.
# - if they are between 3 and 12, the ticket is $10.
# - if they are over the age of 12, the ticket is $15.
#
# 2. Ask a family the age of each person who wants a ticket.
#
# 3. Store the total cost of all the family’s tickets and print it out.
#
# 4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

total = 0
run = True

while run:
    try:
        age = int(input("Please enter your age (enter '200' if you've already entered each family member's age): "))
    except ValueError:
        print("Please enter a number")
    else:
        if not age == 200:
            if age > 12:
                total += 15
            elif age >= 3:
                total += 10
        else:
            print(f"The total cost is: ${total}")
            run = False

names_list = ["John", "Mary", "Mike"]

for name in names_list:
    try:
        teenager_age = int(input(f"{name}, what is your age?\n"))
    except ValueError:
        print("Please enter a number")
    else:
        if 16 <= teenager_age <= 21:
            names_list.remove(name)
            print(f"{name} has been removed from the list")

print(f"The final list is: {', '.join(names_list)}")


# EXERCISE 10
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
#
# 1. Use the above list called sandwich_orders.
# 2. Make an empty list called finished_sandwiches.
# 3. As each sandwich is made, move it to the list of finished sandwiches.
# 4. After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = list()

while len(sandwich_orders) > 0:
    item = sandwich_orders[-1]
    sandwich_orders.remove(item)
    finished_sandwiches.append(item)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")


# EXERCISE 11
# 1. Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# 2. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# 3. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = list()

print("The deli has run out of pastrami")

while len(sandwich_orders) > 0:
    item = sandwich_orders[-1]
    sandwich_orders.remove(item)

    if not item.lower().count('pastrami'):
        finished_sandwiches.append(item)

print(finished_sandwiches)
