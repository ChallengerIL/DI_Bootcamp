# 1. Create a class called Family and implement the following attributes:
#
#   - members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
#   - last_name : (string)
# Initial members data:
#
# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
# 2. Implement the following methods:
#
#   - born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
#   - is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
#   - family_presentation: a method that prints the family’s last name and all the members’ first name.

class Family:

    def __init__(self):
        self.members = [
            {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
            {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
        ]
        self.last_name = 'Smith'

    def born(self, **kwargs):
        new_member = {key: value for key, value in kwargs.items()}
        new_member['is_child'] = True
        new_member['age'] = 0

        self.members.append(new_member)

        print('Congratulations! A new family member has been born!')

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    return True
        return False

    def family_presentation(self):
        print(self.last_name)
        [print(member['name']) for member in self.members]


if __name__ == '__main__':
    family = Family()
    family.born(name='Josh', gender='Male')
    print(family.is_18('Josh'))
    family.family_presentation()
