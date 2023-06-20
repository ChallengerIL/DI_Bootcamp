# Your goal is to create a program to help a city with the vaccination of its citizens.
#
# Part 1
# You will have to create two classes:
# Human
# Queue
#
# Human
# Represents a citizen of the city, it has the following attributes: id_number (str), name (str), age (int), priority (bool) and blood_type (str). Its blood type can be “A”, “B”, “AB” or “O”.
#
# This class has no methods.
#
# Queue
# Represents a queue of humans waiting for their vaccine.
# It has the following attribute : humans, the list containing the humans that are waiting. It is initialized empty.
#
# This class is useful to manage who will get vaccinated in priority. It has the following methods:
#
# add_person(self, person) : Adds a human to the queue, if he is older than 60 years old or a priority person, put him at the beginning of the list (at index 0) before every other.
#
# find_in_queue(self, person) : Returns the index of a human in the queue.
#
# swap(self, person1, person2): Swaps person1 with person2.
#
# get_next(self) : Returns the next human waiting in the queue. The next human should be the one located at the index 0 in the list.
#
# get_next_blood_type(self, blood_type) : Returns the first human with this specific blood type.
#
# sort_by_age(self) : Sorts the queue
# first the priority people
# then, the older people
# then the younger people
# Every human returned by get_next and get_next_blood_type is removed from the list.
# Those functions return None if the list is empty (ie. no one in the list).
#
# Bonus: Don’t use any of the following built-in methods: list.insert, list.pop, list.index, list.sort, sorted.
#
# Part 2
# Human
# Create an attribute family for the Human class.
#
# Initialized as empty, family is a list of all the humans that are living in the same house with this human.
# Add a method add_family_member(self, person) that adds the person to this human’s family and this human to the person’s family.
#
# Queue
# Add the rearange_queue(self) method to the Queue class, so that there won’t be two members of the same family one after the other in the line.

from faker import Faker
from faker.providers import DynamicProvider
from random import randint

POPULATION = 1000
blood_type_provider = DynamicProvider(
     provider_name="blood_type",
     elements=["A", "B", "AB", "O"],
)


class Human:

    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:

    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age > 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        return self.humans.index(person)

    def swap(self, person1, person2):
        person1_idx = self.humans.index(person1)
        person2_idx = self.humans.index(person2)

        self.humans[person1_idx], self.humans[person2_idx] = self.humans[person2_idx], self.humans[person1_idx]

    def get_next(self):
        if len(self.humans) > 0:
            return self.humans.pop(0)
        return None

    def get_next_blood_type(self, blood_type):
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                return self.humans.pop(i)
        return None

    def sort_by_age(self):
        # Young
        for person in self.humans:
            if person.age < 18:
                self.humans.insert(0, self.humans.pop(self.humans.index(person)))

        # Elderly
        for person in self.humans:
            if person.age > 60:
                self.humans.insert(0, self.humans.pop(self.humans.index(person)))

        # Priority
        for person in self.humans:
            if person.priority:
                self.humans.insert(0, self.humans.pop(self.humans.index(person)))

    def rearrange_queue(self):
        for i in range(1, len(self.humans)-1):
            if self.humans[i] in self.humans[i-1].family:
                self.swap(self.humans[i], self.humans[i+1])


if __name__ == "__main__":
    queue = Queue()
    fake = Faker()
    fake.add_provider(blood_type_provider)

    for _ in range(POPULATION):
        human = Human(
            id_number=fake.ssn(), name=fake.name(), age=fake.pyint(max_value=120), priority=fake.pybool(),
            blood_type=fake.blood_type()
        )

        queue.add_person(human)

    # SWAPPING
    # print(queue.humans[0].name)
    # print(queue.humans[-1].name)
    # queue.swap(queue.humans[0], queue.humans[-1])
    # print(queue.humans[0].name)
    # print(queue.humans[-1].name)

    # GET NEXT
    # print(queue.get_next().name)

    # GET NEXT BLOOD TYPE
    # print(queue.get_next_blood_type("AB").name)

    # SORT BY AGE
    # [print(human.name, human.age, human.priority) for human in queue.humans[:50]]
    # print()
    # queue.sort_by_age()
    # [print(human.name, human.age, human.priority) for human in queue.humans[:50]]

    # ADD FAMILY MEMBER
    # for idx in range(len(queue.humans)-1):
    #     if randint(0, 20) == 0:
    #         queue.humans[idx].add_family_member(queue.humans[idx+1])

    # REARRANGE QUEUE
    # [print(human.name, queue.humans.index(human)) for human in queue.humans if len(human.family) > 0]
    # print()
    # queue.rearrange_queue()
    # [print(human.name, queue.humans.index(human)) for human in queue.humans if len(human.family) > 0]
