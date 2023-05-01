# 1. Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

target_name = "Iurii"
run = True

while run:
    user_name = input("What is your name?\n").title()
    
    if user_name == target_name:
        run = False
