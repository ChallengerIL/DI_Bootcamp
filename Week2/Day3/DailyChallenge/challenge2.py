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
