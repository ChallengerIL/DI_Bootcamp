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
    