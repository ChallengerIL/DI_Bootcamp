user_height = float(input("Enter your height in inches: "))
cm_height = user_height * 2.54

if cm_height >= 145:
    print("Great! You are tall enough to ride!")
else:
    print("We are sorry but you are not tall enough for the ride.")

