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
        for sub in ramat_gan_safari.animals:
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
