# 1. Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# 2. As they enter each topping, print a message saying you’ll add that topping to their pizza.
# 3. Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

PIZZA_PRICE = 10

run = True
toppings = list()

while run:
    topping = input("What toppings would you like?\n")
    if topping == "quit":
        run = False
    else:
        print(f"We will add {topping} to your pizza.")
        toppings.append(topping)

print(f"Your pizza toppings will include: {', '.join(toppings)}")

toppings_price = len(toppings) * 2.5

print(f"Your total pizza price is ${PIZZA_PRICE + toppings_price}")
