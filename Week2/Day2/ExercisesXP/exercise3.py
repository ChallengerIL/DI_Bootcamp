# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# 1. Remove “Banana” from the list.
# 2. Remove “Blueberries” from the list.
# 3. Add “Kiwi” to the end of the list.
# 4. Add “Apples” to the beginning of the list.
# 5. Count how many apples are in the basket.
# 6. Empty the basket.
# 7. Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.pop(0)
basket.pop(-1)
basket.append("Kiwi")
basket.insert(0, "Apples")
print(f"There are this many apples in the basket: {basket.count('Apples')}")
basket.clear()
print(basket)
