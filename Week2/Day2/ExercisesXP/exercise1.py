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

print(f"My friend’s fav numbers: {friend_fav_numbers}")

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(f"Our fav numbers: {our_fav_numbers}")
