# EXERCISE 1
# 1. Convert the two following lists, into dictionaries.
# Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = zip(keys, values)


print(dict(result))


# EXERCISE 2
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


# EXERCISE 3
# 1. Here is some information about a brand.
# - name: Zara
# - creation_date: 1975
# - creator_name: Amancio Ortega Gaona
# - type_of_clothes: men, women, children, home
# - international_competitors: Gap, H&M, Benetton
# - number_stores: 7000
# - major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
#
# - creation_date: 1975
# - number_stores: 10 000
#
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

# 2
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": ["blue"],
        "Spain": ["red"],
        "US": ["pink", "green"],
    }
}

# 3
brand["number_stores"] = 2

# 4
print(f"Zara's clients are: {brand['type_of_clothes'][0]}, {brand['type_of_clothes'][1]} and {brand['type_of_clothes'][2]}")

# 5
brand["country_creation"] = "Spain"

# 6
if "international_competitors" in brand.keys():
    brand["international_competitors"].append("Desigual")

# 7
brand.pop("creation_date")

# 8
print(brand["international_competitors"][-1])

# 9
print("The major clothes colors in the US are:")
[print(color) for color in brand["major_color"]["US"]]

# 10
print(len(brand))

# 11
[print(key) for key in brand.keys()]

# 12
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10_000,
}

# 13
brand.update(more_on_zara)

# 14
print(brand["number_stores"])
# We updated our initial dictionary with the information from the last one.


# EXERCISE 4
# Use this list :
#
# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :
#
# #1/
#
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#
# #2/
#
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
# #3/
#
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
#
#
# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# 2. Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# 3. Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# 4. Only recreate the 1st result for:
#     1. The characters, which names contain the letter “i”.
#     2. The characters, which names start with the letter “m” or “p”.

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {}
disney_users_B = {}
disney_users_C = {}

# 1, 2
for idx, user in enumerate(users):
    disney_users_A[user] = idx
    disney_users_B[idx] = user

print(disney_users_A)
print("\n")
print(disney_users_B)
print("\n")

# 3
our_keys = list(disney_users_A.keys())
our_keys.sort()

for idx, user in enumerate(our_keys):
    disney_users_C[user] = idx

print(disney_users_C)
print("\n")

# 4
final_dict_1 = dict()

users_list = [user for user in users if "i" in user.lower()]

for idx, user in enumerate(users_list):
    if "i" in user.lower():
        final_dict_1[user] = idx

print(final_dict_1)
print("\n")

# 5
final_dict_2 = dict()

users_list = [user for user in users if "m" == user[0].lower() or "p" == user[0].lower()]

for idx, user in enumerate(users_list):
    if "m" == user[0].lower() or "p" == user[0].lower():
        final_dict_2[user] = idx

print(final_dict_2)
