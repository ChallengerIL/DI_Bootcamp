# 1. Take a look at the following code and output:
# File: market.py
#
# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# Output
#
# McDonald's farm
#
# cow : 5
# sheep : 2
# goat : 12
#
#     E-I-E-I-0!
#
#
# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:
#
# 1. Create a class called Farm. How should it be implemented?
# 2. Does the Farm class need an __init__ method? If so, what parameters should it take?
# 3. How many methods does the Farm class need?
# 4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
# 5. Test your code and make sure you get the same results as the example above.
# 6. Bonus: nicely line the text in columns as seen in the example above. Use string formatting.
#
#
# Expand The Farm
# 1. Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].
#
# 2. Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, amount=1):
        if animal not in self.animals.keys():
            self.animals[animal] = amount
        else:
            self.animals[animal] += amount

    def get_info(self):
        print(f"{self.name}'s farm\n")

        [print(f"{animal} : {amount}") for animal, amount in self.animals.items()]

        print(f"\n\tE-I-E-I-O!")

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animals = self.get_animal_types()

        return "{}'s farm has {} and {}".format(self.name, ", ".join(animals[:-1]), animals[-1])


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.get_info()

print(macdonald.get_animal_types())
print(macdonald.get_short_info())
