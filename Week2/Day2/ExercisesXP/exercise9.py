# 1. A movie theater charges different ticket prices depending on a person’s age.
# - if a person is under the age of 3, the ticket is free.
# - if they are between 3 and 12, the ticket is $10.
# - if they are over the age of 12, the ticket is $15.
#
# 2. Ask a family the age of each person who wants a ticket.
#
# 3. Store the total cost of all the family’s tickets and print it out.
#
# 4. A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

total = 0
run = True

while run:
    try:
        age = int(input("Please enter your age (enter '200' if you've already entered each family member's age): "))
    except ValueError:
        print("Please enter a number")
    else:
        if not age == 200:
            if age > 12:
                total += 15
            elif age >= 3:
                total += 10
        else:
            print(f"The total cost is: ${total}")
            run = False

names_list = ["John", "Mary", "Mike"]

for name in names_list:
    try:
        teenager_age = int(input(f"{name}, what is your age?\n"))
    except ValueError:
        print("Please enter a number")
    else:
        if 16 <= teenager_age <= 21:
            names_list.remove(name)
            print(f"{name} has been removed from the list")

print(f"The final list is: {', '.join(names_list)}")
