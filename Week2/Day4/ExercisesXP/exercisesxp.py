# EXERCISE 1
# 1. Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# 2. Call the function, and make sure the message displays correctly.


def display_message():
    print("I am learning Python")


if __name__ == "__main__":
    display_message()


# EXERCISE 2
# 1. Write a function called favorite_book() that accepts one parameter called title.
# 2. The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# 3. Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f"One of my favorite books is {title}")


if __name__ == "__main__":
    favorite_book("Alice in Wonderland")


# EXERCISE 3
# 1. Write a function called describe_city() that accepts the city of a city and its country as parameters.
# 2. The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# 3. Give the country parameter a default value.
# 4. Call your function.

def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")


if __name__ == "__main__":
    describe_city("Reykjavik", "Iceland")


# EXERCISE 4
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


# EXERCISE 5
# 1. Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# 2. The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# 3. Call the function make_shirt().
# 4. Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# 5. Make a large shirt with the default message
# 6. Make medium shirt with the default message
# 7. Make a shirt of any size with a different message.
# 8. Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size: str = "large", message: str = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {message}")


make_shirt()
make_shirt("medium")
make_shirt("small", "I don't like CSS")
make_shirt(size="extra-large", message="I love Israel")


# EXERCISE 6
# 1. Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# 2. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# 3. Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# 4. Call the function make_great().
# 5. Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(names_list: list):
    return [print(name) for name in names_list]


def make_great():
    global magician_names
    # return [name + "the Great" for name in names_list]

    for name in magician_names:
        idx = magician_names.index(name)
        name += " the Great"
        magician_names[idx] = name


if __name__ == '__main__':
    show_magicians(magician_names)
    print("\n")
    make_great()
    show_magicians(magician_names)


# EXERCISE 7
# 1. Create a function called get_random_temp().
#     1. This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#     2. Test your function to make sure it generates expected results.
#
# 2. Create a function called main().
#     1. Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#     2. Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
#
# 3. Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#     1. below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#     2. between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#     3. between 16 and 23
#     4. between 24 and 32
#     5. between 32 and 40
#
# 4. Change the get_random_temp() function:
#     1. Add a parameter to the function, named ‘season’.
#     2. Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
#     3. Now that we’ve changed get_random_temp(), let’s change the main() function:
#         1. Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#         2. Use the season as an argument when calling get_random_temp().
#
# 5. Bonus: Give the temperature as a floating-point number instead of an integer.
# 6. Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

import random

SEASONS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


def get_random_temp(season: int):
    lower = -10
    upper = 40

    season = SEASONS[season]

    if season == 'spring':
        lower = 10
        upper = 30
    elif season == 'summer':
        lower = 20
        upper = 40
    elif season == 'autumn' or season == 'fall':
        lower = 20
        upper = 35
    elif season == 'winter':
        lower = -10
        upper = 16

    return round(random.uniform(lower, upper), 1)


def main():
    season = int()

    try:
        season = int(input("What season would you like to know the temperature in (provide the month as a"
                           " number)?\n"))
    except ValueError:
        print("Please enter a number")

    temp = get_random_temp(season)
    print(f'The temperature right now is {temp} degrees Celsius.')

    if temp > 32:
        print("It's hot today, don't forget your water")
    elif temp > 23:
        print("The temperature is great! Enjoy your day!")
    elif temp > 15:
        print('The temperature is fine')
    elif temp > -1:
        print("Quite chilly! Don't forget your coat")
    else:
        print("Brrr, that's freezing! Wear some extra layers today")


if __name__ == '__main__':
    main()
