# EXERCISE 2
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


# EXERCISE 3
# 1. Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
import string
from random import choices

LENGTH = 5


def random_string():
    return ''.join(choices(string.ascii_uppercase + string.ascii_lowercase, k=LENGTH))


if __name__ == '__main__':
    print(random_string())


# EXERCISE 4
# 1. Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import date


def display_date():
    print(date.today())


if __name__ == '__main__':
    display_date()


# EXERCISE 5
# 1. Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

import datetime as dt


def time_left():
    present = dt.datetime.now()
    future = dt.datetime(dt.date.today().year + 1, 1, 1, 0, 0, 0)
    difference = future - present
    print(f"The 1st of January is in {difference}")


if __name__ == "__main__":
    time_left()


# EXERCISE 6
# 1. Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime


def time_lived(birthdate: str):
    now = datetime.now()
    age = now - datetime.strptime(birthdate, '%Y-%m-%d')
    minutes = int(age.total_seconds() // 60)
    print(f'You have lived {minutes} minutes.')


if __name__ == '__main__':
    birthdate_input = "2001-12-30"

    time_lived(birthdate_input)


# EXERCISE 7
# 1. Write a function that displays today’s date.
# 2. The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

import datetime
import holidays


def date_now():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def get_next_holiday(country_code: str = "IL", days_num: int = 300):
    holidays_holder = holidays.country_holidays(country_code)

    base = datetime.datetime.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(days_num)]

    upcoming_holidays_list = [date for date in date_list if date in holidays_holder]

    return upcoming_holidays_list[0], holidays_holder.get(upcoming_holidays_list[0])


def next_holiday_time_left():
    next_holiday_date, next_holiday_name = get_next_holiday()
    time_left = next_holiday_date - datetime.datetime.now()

    print(f"The next holiday is {next_holiday_name} which occurs on {next_holiday_date.date()} and {time_left} is left.")


if __name__ == '__main__':
    next_holiday_time_left()
    

# EXERCISE 8
# 1. Given an age in seconds, calculate how old someone would be on:
#   - Earth: orbital period 365.25 Earth days, or 31557600 seconds
#   - Mercury: orbital period 0.2408467 Earth years
#   - Venus: orbital period 0.61519726 Earth years
#   - Mars: orbital period 1.8808158 Earth years
#   - Jupiter: orbital period 11.862615 Earth years
#   - Saturn: orbital period 29.447498 Earth years
#   - Uranus: orbital period 84.016846 Earth years
#   - Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.

AGE_SECONDS = 1_000_000_000
SECONDS_IN_A_DAY = 86_400
EARTH_YEAR = 365.25


def calculate_celestial_age(planet: str, age_seconds: int):
    planets_data = {
        "mercury": 0.2408467, "venus": 0.61519726, "earth": 1, "mars": 1.8808158,
        "jupiter": 11.862615, "saturn": 29.447498, "uranus": 84.016846, "neptune": 164.79132,
    }

    if planet.lower() in planets_data:
        return round(((age_seconds / SECONDS_IN_A_DAY) / EARTH_YEAR) * planets_data[planet], 2)

    raise Exception("Unknown Planet! Try again...")


if __name__ == "__main__":
    print(calculate_celestial_age("earth", AGE_SECONDS))
    print(calculate_celestial_age("earth", 31557600))
    print(calculate_celestial_age("mars", AGE_SECONDS))


# EXERCISE 9
# 1. Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# 2. Create an empty list called users. Tip: It should be a list of dictionaries.
# 3. Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker

users = []


def add_user(name, address, language_code):
    new_user = {"name": name, "address": address, "language_code": language_code}
    users.append(new_user)


if __name__ == '__main__':
    fake_user = Faker()
    
    for i in range(10):
        add_user(fake_user.name(), fake_user.address(), fake_user.language_code())

    print(users)
