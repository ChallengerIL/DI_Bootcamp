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
