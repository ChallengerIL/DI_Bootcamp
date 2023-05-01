# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
#
# 1. Use the above list called sandwich_orders.
# 2. Make an empty list called finished_sandwiches.
# 3. As each sandwich is made, move it to the list of finished sandwiches.
# 4. After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = list()

while len(sandwich_orders) > 0:
    item = sandwich_orders[-1]
    sandwich_orders.remove(item)
    finished_sandwiches.append(item)

for sandwich in finished_sandwiches:
    print(f"I made your {sandwich}")
