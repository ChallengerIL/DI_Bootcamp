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
