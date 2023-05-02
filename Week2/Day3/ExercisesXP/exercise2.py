# 1. A movie theater charges different ticket prices depending on a person’s age.
# - if a person is under the age of 3, the ticket is free.
# - if they are between 3 and 12, the ticket is $10.
# - if they are over the age of 12, the ticket is $15.
#
# 2. Given the following object:
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
#
# 3. How much does each family member have to pay ?
#
# 4. Print out the family’s total cost for the movies.
# 5. Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


def get_price(visitors_dict):
    price_dict = dict()
    total_price = 0

    if len(visitors_dict) > 0:
        for name, age in visitors_dict.items():
            if age > 12:
                price_dict[name] = 15
            elif 3 <= age <= 12:
                price_dict[name] = 10
            else:
                price_dict[name] = 0

        total_price = sum(price_dict.values())

    return price_dict, total_price


def get_receipt(prices):

    for client_name, price in prices[0].items():
        print(f"{client_name} has to pay ${price}")

    print(f"The total price for the family is ${prices[-1]}")


get_receipt(get_price(family))

run = True
family = dict()

while run:
    should_stop = input("Do you want to stop? (y/n): ").lower()[0]
    if should_stop == "y":
        run = False
        break

    user_name = input("Enter your name: ").strip()
    user_age = int(input("Enter your age: "))

    family[user_name] = user_age

get_receipt(get_price(family))
