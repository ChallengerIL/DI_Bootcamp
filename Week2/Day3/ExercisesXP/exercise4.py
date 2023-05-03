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
