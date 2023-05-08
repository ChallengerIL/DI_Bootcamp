# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.
#
#
#
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
#
#   1. Create a class called Text that takes a string as an argument and store the text in a attribute.
#   Hint: You need to manually copy-paste the text, straight into the code
#
#   2. Implement the following methods:
#       - a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
#       - a method that returns the most common word in the text.
#       - a method that returns a list of all the unique words in the text.
#
#
# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
#
#   1. Implement a classmethod that returns a Text instance but with a text file:
#
#       >>> Text.from_file('the_stranger.txt')
#   Hint: You need to open and read the text from the text file.
#
#
#   2. Now, use the provided the_stranger.txt file and try using the class you created above.
#
#
#
# Bonus:
#   1. Create a class called TextModification that inherits from Text.
#
#   2. Implement the following methods:
#       - a method that returns the text without any punctuation.
#       - a method that returns the text without any english stop-words (check out what this is !!).
#       - a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

import re
from gensim.parsing.preprocessing import remove_stopwords
from os.path import dirname, join

CURRENT_DIR = dirname(__file__)
TEXT_FILE = "./the_stranger.txt"
FILE_PATH = join(CURRENT_DIR, TEXT_FILE)
STRING = "A good book would sometimes cost as much as a good house."


class Text:

    def __init__(self, text):
        self.text = text

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            return cls(f.read())


class TextAnalysis:

    def __init__(self, text):
        self.text_list = text.split()

    def count_occurrences(self, word):
        if word not in self.text_list:
            return print("The word is not present in the text.")

        return self.text_list.count(word)

    def find_most_common_word(self):
        return max(set(self.text_list), key=self.text_list.count)

    def get_unique_words(self):
        lowered_list = [word.lower() for word in self.text_list]
        return list(set(lowered_list))


class TextModification(Text):

    def __init__(self, text):
        super().__init__(text)

    # Remove punctuation
    def clean_text(self):
        return re.sub(r'[^\w\s]', '', self.text)

    def remove_stop_words(self):
        return remove_stopwords(self.text)

    def remove_special_characters(self):
        return ''.join(letter for letter in self.text if letter.isalnum())


if __name__ == "__main__":
    txt = Text(STRING)

    text_analysis = TextAnalysis(txt.text)
    # print(text_analysis.count_occurrences("good"))
    # print(text_analysis.find_most_common_word())
    # print(text_analysis.get_unique_words())
    # print(text_analysis.text_list)

    external_text = Text.from_file(TEXT_FILE).text
    external_text_analysis = TextAnalysis(external_text)
    # print(external_text_analysis.text_list)
    # print(external_text_analysis.count_occurrences("good"))
    # print(external_text_analysis.find_most_common_word())
    # print(external_text_analysis.get_unique_words())
    # print(external_text_analysis.text_list)

    text_modification = TextModification(external_text)
    # text_modification.clean_text()
    # text_modification.remove_stop_words()
    # print(text_modification.remove_special_characters())
