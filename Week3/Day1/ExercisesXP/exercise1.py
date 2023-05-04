# Using this class
#
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#
# 1. Instantiate three Cat objects using the code provided above.
# 2. Outside of the class, create a function that finds the oldest cat and returns the cat.
# 3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

from operator import attrgetter


class Cat:
    cats_list = []

    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        Cat.cats_list.append(self)


def find_oldest_cat(cat_list):
    oldest_cat = max(cat_list, key=attrgetter('age'))
    print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")


if __name__ == "__main__":
    cat_1 = Cat("Fido", 3)
    cat_2 = Cat("Milo", 1)
    cat_3 = Cat("Garfield", 2)

    find_oldest_cat(Cat.cats_list)
