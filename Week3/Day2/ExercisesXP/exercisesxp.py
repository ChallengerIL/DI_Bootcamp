# EXERCISE 1
# Using this code:
#
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# 1. Create another cat breed named Siamese which inherits from the Cat class.
# 2. Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# 3. Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# 4. Take all the cats for a walk, use the walk method.

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


bengal = Bengal('Bengal', 1)
chartreux = Chartreux('Chartreux', 2)
siamese = Siamese('Siamese', 5)

all_cats = [bengal, chartreux, siamese]

sara_pets = Pets(all_cats)
sara_pets.walk()


# EXERCISE 2
# 1. Create a class called Dog with the following attributes name, age, weight.
# 2. Implement the following methods in the Dog class:
#   - bark: returns a string which states: “<dog_name> is barking”.
#   - run_speed: returns the dogs running speed (weight/age*10).
#   - fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
#
# 3. Create 3 dogs and run them through your class.

class Dog:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight/self.age*10

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight with {other_dog.name}"
        else:
            return f"{other_dog.name} won the fight with {self.name}"


if __name__ == "__main__":
    dog_1 = Dog("Fido", 2, 10)
    dog_2 = Dog("Milo", 3, 15)
    dog_3 = Dog("Buddy", 10, 19)

    print(dog_1.bark())
    print(dog_2.run_speed())
    print(dog_3.fight(dog_1))


# EXERCISE 3
# 1. Create a new python file and import your Dog class from the previous exercise.
# 2. In the new python file, create a class named PetDog that inherits from Dog.
# 3. Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# 4. Add the following methods:
#   - train: prints the output of bark and switches the trained boolean to True
#
#   - play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
#
#   - do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#       - “dog_name does a barrel roll”.
#       - “dog_name stands on his back legs”.
#       - “dog_name shakes your hand”.
#       - “dog_name plays dead”.

# from exercise2 import Dog
import random


class PetDog(Dog):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        print("{} all play together".format(', '.join(map(str, dog_names))))

    def do_a_trick(self):
        tricks = [
            f"{self.name} does a barrel roll",
            f"{self.name} stands on his back legs",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead",
        ]

        if self.trained:
            print(random.choice(tricks))


if __name__ == '__main__':
    dog_1 = PetDog(name="Larry", age=4, weight=13)
    dog_2 = PetDog(name="Mary", age=3, weight=12)
    dog_3 = PetDog(name="Spot", age=7, weight=10)

    dog_1.do_a_trick()
    dog_1.play(dog_1.name, dog_2.name, dog_3.name)
    dog_1.train()
    dog_1.do_a_trick()
    