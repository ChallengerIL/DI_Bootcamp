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
