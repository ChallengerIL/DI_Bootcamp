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
