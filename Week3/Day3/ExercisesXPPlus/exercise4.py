# 1. Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import date


def display_date():
    print(date.today())


if __name__ == '__main__':
    display_date()
