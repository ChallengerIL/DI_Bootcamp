# CHALLENGE 1
# 1. Ask a user for a word
# 2. Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# - Make sure the letters are the keys.
# - Make sure the letters are strings.
# - Make sure the indexes are stored in a list and those lists are values.
#
# Examples
# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

from collections import defaultdict

users_word = input("Enter a word: ").strip().lower()

d = defaultdict(list)
for idx, letter in enumerate(users_word):
    d[letter].append(idx)

d = dict(d)

print(d)


# CHALLENGE 2
# 1. Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# 2. Sort the list in alphabetical order.
# 3. Return “Nothing” if you can’t afford anything from the store.
#
# Examples
#
# The key is the product, the value is the price
#
# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }
#
# wallet = "$300"
#
# ➞ ["Bread", "Fertilizer", "Water"]
#
# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }
#
# wallet = "$100"
#
# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]
#
# items_purchase = {
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"
# }
#
# wallet = "$1"
#
# ➞ "Nothing"

import re


class Wallet:

    def __init__(self, money: int):
        self.total_money = money
        self.can_afford_list = list()

    def check_if_can_afford(self, items_dict: dict):
        for key, value in items_dict.items():
            value = int(re.findall(r'\d+', value)[0])

            if self.total_money >= value:
                self.can_afford_list.append(key)

        if len(self.can_afford_list) > 0:
            self.can_afford_list.sort()
            print(self.can_afford_list)
        else:
            return print("Nothing")


items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = Wallet(90)

wallet.check_if_can_afford(items_purchase)
