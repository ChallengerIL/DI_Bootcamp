# 1. Ask the user for a number and a length.
# 2. Create a program that prints a list of multiples of the number until the list length reaches length.

input_number = int(input("Enter a number: "))
input_length = int(input("Enter a length: "))
result = list()


def multiples(n, length):
    result.append(n)

    while len(result) < length:
        result.append(result[-1] + n)
        print(result)


multiples(input_number, input_length)
