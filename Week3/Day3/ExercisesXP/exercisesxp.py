# EXERCISE 1
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.
#
# 1. Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# 2. Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.

class BuiltInPrint:
    """
    The print_abs() method prints the absolute value of a number.

    The print_int() method prints the integer value of a number.

    The print_input() method prints the input from the user.
    """

    def print_abs(self, number):
        print(abs(number))

    def print_int(self, number):
        print(int(number))

    def print_input(self):
        print(input("Type something here: "))


if __name__ == "__main__":
    func_instance = BuiltInPrint()
    func_instance.print_abs(2)
    func_instance.print_int(342)
    func_instance.print_input()

    print(func_instance.__doc__)


# EXERCISE 2
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
#
#     #Your code starts HERE
#
#
# 1. Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)
#
# >>> str(c1)
# '5 dollars'
#
# >>> int(c1)
# 5
#
# >>> repr(c1)
# '5 dollars'
#
# >>> c1 + 5
# 10
#
# >>> c1 + c2
# 15
#
# >>> c1
# 5 dollars
#
# >>> c1 += 5
# >>> c1
# 10 dollars
#
# >>> c1 += c2
# >>> c1
# 20 dollars
#
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}'

    def __add__(self, other):
        if isinstance(other, Currency):
            if other.currency != self.currency:
                raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')

            return Currency(self.currency, self.amount + other.amount)

        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)


if __name__ == '__main__':
    c1 = Currency('dollar', 5)
    c2 = Currency('dollar', 10)
    c3 = Currency('shekel', 1)
    c4 = Currency('shekel', 10)

    print(str(c1))
    # '5 dollars'

    print(int(c1))
    # 5

    print(repr(c1))
    # '5 dollars'

    print(c1 + 5)
    # 10

    print(c1 + c2)
    # 15

    print(c1)
    # 5 dollars

    c1 += 5
    print(c1)
    # 10 dollars

    c1 += c2
    print(c1)
    # 20 dollars

    c1 + c3
    # TypeError: Cannot add between Currency type < dollar > and < shekel >
