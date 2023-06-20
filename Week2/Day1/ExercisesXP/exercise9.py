# 1. Write code that will ask the user for their height in inches.
# 2. If they are over 145cm print a message that states they are tall enough to ride.
# 3. If they are not tall enough print a message that says they need to grow some more to ride.

user_height = float(input("Enter your height in inches: "))
cm_height = user_height * 2.54

if cm_height >= 145:
    print("Great! You are tall enough to ride!")
else:
    print("We are sorry but you are not tall enough for the ride.")

