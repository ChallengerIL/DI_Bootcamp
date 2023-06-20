# 1. Using the input function, ask the user for a string. The string must be 10 characters long.
# -If it’s less than 10 characters, print a message which states “string not long enough”.
# -If it’s more than 10 characters, print a message which states “string too long”.
# 2. Then, print the first and last characters of the given text.
# 3. Using a for loop, construct the string character by character: Print the first character, then the second,
# then the third, until the full string is printed.
# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).

import random

run = True
result = list()

while run:
    user_input = input("Enter your string: ")

    if user_input.lower() == "quit":
        run = False
        break

    # Count the length without the spaces
    length = len(''.join([char for char in user_input if char != ' ']))

    if length < 10:
        print("string not long enough")
    if length > 10:
        print("string too long")
    else:
        print(f"The first character is {user_input[0]} and the last one is {user_input[-1]}")
        for char in user_input:
            result += char
            print("".join(result))

    random.shuffle(result)
    print("".join(result))
