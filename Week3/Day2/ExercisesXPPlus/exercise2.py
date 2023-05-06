# 1. Create a class called TheIncredibles. This class should inherit from the Family class:
#
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:
#
# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]
#
#
# 2. Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
#
#
# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.
#
#
# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.

from exercise1 import Family


class TheIncredibles(Family):

    def __init__(self):
        super().__init__()
        # self.members[0]['power'] = 'fly'
        # self.members[0]['incredible_name'] = 'MikeFly'
        # self.members[1]['power'] ='read minds'
        # self.members[1]['incredible_name'] = 'SuperWoman'
        self.members = [
            {
                'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly',
                'incredible_name': 'MikeFly',
            },
            {
                'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds',
                'incredible_name': 'SuperWoman',
            },
        ]

    # def use_power(self, name):
    #     for member in self.members:
    #         if member['name'] == name:
    #             if member['age'] >= 18:
    #                 print(member['name'], member['power'])
    #             else:
    #                 raise Exception(f"{member['name']} is not over 18 years old")

    def use_power(self):
        for member in self.members:
            if member['age'] >= 18:
                print(member['name'], member['power'])
            else:
                raise Exception(f"{member['name']} is not over 18 years old")

    def incredible_presentation(self):
        super().family_presentation()

        [print(member['name'], member['power']) for member in self.members]


if __name__ == '__main__':
    incredibles = TheIncredibles()

    # incredibles.use_power()
    incredibles.incredible_presentation()
    incredibles.born(name='Jack', gender='Male', power='Unknown Power')
    incredibles.incredible_presentation()
