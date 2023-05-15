# EXERCISE 1
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


# EXERCISE 2
# 1. Create a class called Dog.
# 2. In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# 3. Create a method called bark that prints the following string “<dog_name> goes woof!”.
# 4. Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# 5. Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# 6. Print the details of his dog (ie. name and height) and call the methods bark and jump.
# 7. Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# 8. Print the details of her dog (ie. name and height) and call the methods bark and jump.
# 9. Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

from operator import attrgetter


class Dog:

    dogs_list = []

    def __init__(self, name, height):
        self.name = name
        self.height = height
        Dog.dogs_list.append(self)

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")


davids_dog = Dog("Rex", 50)
print(f"David's dog's name is {davids_dog.name} and his height is {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()
print("\n")

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog's name is {sarahs_dog.name} and it's height is {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()
print("\n")

biggest_dog = max(Dog.dogs_list, key=attrgetter('height'))

print(f"The bigger dog's name is {davids_dog.name}.")


# EXERCISE 3
# 1. Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# 3. Create an object, for example:
#
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#
# 4. Then, call the sing_me_a_song method. The output should be:
#
# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        [print(line) for line in self.lyrics]


if __name__ == '__main__':
    stairway = Song(["There's a lady who's sure", "all that glitters is gold", "and she's buying a stairway to heaven"])

    stairway.sing_me_a_song()


# EXERCISE 4
# 1. Create a class called Zoo.
# 2. In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the ramat_gan_safari).
# 3. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# 4. Create a method called get_animals that prints all the animals of the ramat_gan_safari.
# 5. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# 6. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example
#
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
#
#
# 7. Create a method called get_groups that prints the animal/animals inside each group.
#
# 8. Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the ramat_gan_safari --> Giraffe
# x.add_animal(Giraffe)

def util_func(x, y):
    return x[0] == y[0]


class Zoo:

    def __init__(self, zoo_name):
        self.animals = []
        self.animals_dict = {}
        self.name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        self.animals.sort()

        res = []
        for sub in self.animals:
            ele = next((x for x in res if util_func(sub, x[0])), [])
            if not ele:
                res.append(ele)
            ele.append(sub)

        for i, name in enumerate(res):
            self.animals_dict[i] = name

    def get_groups(self):
        for value in self.animals_dict.values():
            print(value)


ramat_gan_safari = Zoo("Ramat Gan Safari")

animals = ["Giraffe", "Cougar", "Bear", "Ape", "Eel", "Emu", "Baboon", "Cat"]

[ramat_gan_safari.add_animal(animal) for animal in animals]

ramat_gan_safari.get_animals()

ramat_gan_safari.sell_animal("Eel")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
