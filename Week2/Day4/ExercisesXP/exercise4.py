# 1. Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

START = 1
END = 100


def number_generator(users_num: int):
    number = random.randint(START, END)

    if users_num == number:
        print('Success! The two numbers have matched!')
    else:
        print(f'Fail! The two numbers do not match! Your number is {users_num} and the random number is {number}')


if __name__ == '__main__':
    try:
        users_input = int(input('Enter a number between 1 and 100: '))
    except ValueError:
        print('Wrong input. Please enter a number between 1 and 100.')
    else:
        number_generator(users_input)
