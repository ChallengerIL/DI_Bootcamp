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
