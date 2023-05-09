# First Download this text file : right click –> Save As
#
# 1. Create a new file called anagram_checker.py which contains a class called AnagramChecker.
#
# 2. The class should have the following methods:
#   - __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
#   - is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.
#
#   - get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)
#
#   - Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
#
#   - Note: None of the methods in the class should print anything.
#
# 3. Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.
#
# 4. It should do the following:
#       1. Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
#
#       2. If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
#           - Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
#           - Only alphabetic characters are allowed. No numbers or special characters.
#           - Whitespace should be removed from the start and end of the user’s input.
#
#       3. Once your code has decided that the user’s input is valid, it should find out the following:
#           - All possible anagrams to the user’s word.
#           - Create an AnagramChecker instance and apply it to the steps created above.
#           - Display the information about the word in a user-friendly, nicely-formatted message such as:
#
#
#           YOUR WORD :”MEAT”
#           this is a valid English word.
#           Anagrams for your word: mate, tame, team.

from os.path import dirname, join
import itertools

CURRENT_DIR = dirname(__file__)
TEXT_FILE = "./sowpods.txt"
FILE_PATH = join(CURRENT_DIR, TEXT_FILE)


class AnagramChecker:

    def __init__(self, word_list_file: str = FILE_PATH):
        with open(word_list_file) as f:
            self.word_list = f.read().splitlines()

    def is_valid_word(self, word: str):
        if word in self.word_list:
            return True

        return False

    def get_anagrams(self, word: str):
        word = word.strip().upper()

        anagrams = list(map("".join, itertools.permutations(word)))
        real_anagrams = list()

        for anagram in anagrams:
            if self.is_valid_word(anagram):
                real_anagrams.append(anagram.lower())

        return real_anagrams

    def is_anagram(self, word1: str, word2: str):
        return sorted(word1) == sorted(word2)


if __name__ == "__main__":
    checker = AnagramChecker()
