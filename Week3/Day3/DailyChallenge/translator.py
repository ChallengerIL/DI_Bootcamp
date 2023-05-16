# TRANSLATOR
# Consider this list
#
# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# 1. Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.

from googletrans import Translator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]


if __name__ == "__main__":
    translator = Translator()
    translation_dict = {word: translator.translate(word, src='fr', dest='en').text for word in french_words}
    print(translation_dict)
