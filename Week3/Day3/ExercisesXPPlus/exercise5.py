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
