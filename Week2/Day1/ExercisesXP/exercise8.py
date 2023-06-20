# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

base_name = "Iurii"
user_name = input("Please enter your name: ").title()

if base_name == user_name:
    print("Awesome! We have the same name!")
else:
    print("Our names are different... What a shame.")
