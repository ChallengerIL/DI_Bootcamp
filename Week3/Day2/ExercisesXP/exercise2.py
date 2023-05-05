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


dog_1 = Dog("Fido", 2, 10)
dog_2 = Dog("Milo", 3, 15)
dog_3 = Dog("Buddy", 10, 19)

print(dog_1.bark())
print(dog_2.run_speed())
print(dog_3.fight(dog_1))
