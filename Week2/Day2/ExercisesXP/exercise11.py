# 1. Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# 2. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# 3. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = list()

print("The deli has run out of pastrami")

while len(sandwich_orders) > 0:
    item = sandwich_orders[-1]
    sandwich_orders.remove(item)

    if not item.lower().count('pastrami'):
        finished_sandwiches.append(item)

print(finished_sandwiches)
