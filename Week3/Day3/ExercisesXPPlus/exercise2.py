# 1. Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
#     - if it’s the same number, display a success message to the user, else don’t.

from random import randint


def roll_dice(num: int):
    if 0 < num < 101:
        random_num = randint(1, 100)

        if num == random_num:
            print("Success!")


if __name__ == "__main__":
    roll_dice(randint(1, 100))
