# 1. Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.

import re


def remove_consecutive_duplicates(s):
    return re.sub(r'(.)\1+', r'\1', s)


user_input = input('Enter a string: ')

print(remove_consecutive_duplicates(user_input))
