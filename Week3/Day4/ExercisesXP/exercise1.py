# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
#
# Hint : The generated sentences do not have to make sense.
#
# 1. Download this word list
#
# 2. Save it in your development directory.
#
# 3. Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
#
# 4. Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
#   - use the words list to get your random words.
#   - the amount of words should be the value of the length parameter.
#
# 5. Take the random words and create a sentence (using a python method), the sentence should be lower case.
#
# 6. Create a function called main which will:
#
#   1. Print a message explaining what the program does.
#
#   2. Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
#       - If the user inputs incorrect data, print an error message and end the program.
#       - If the user inputs correct data, run your code.

import random
from os.path import dirname, join

CURRENT_DIR = dirname(__file__)
TEXT_FILE = "./sowpods.txt"
FILE_PATH = join(CURRENT_DIR, TEXT_FILE)


def get_words_from_file(filename):
    with open(filename) as f:
        return f.read().split()


def get_random_sentence(length: int):
    words = get_words_from_file(FILE_PATH)
    words_lower = [word.lower() for word in words]
    return " ".join(random.sample(words_lower, length))


def main():
    print("This program will generate a random sentence.")
    try:
        length = int(input("How long should the sentence be? "))
    except ValueError:
        print("Please enter an integer between 2 and 20.")
    else:
        if 2 <= length <= 20:
            print(get_random_sentence(length))
        else:
            raise Exception("Please enter an integer between 2 and 20.")


if __name__ == "__main__":
    main()
