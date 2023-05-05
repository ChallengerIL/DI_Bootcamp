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

from exercise2 import Dog
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
    