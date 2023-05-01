# 1. Use a for loop to print all numbers from 1 to 20, inclusive.
# 2. Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# 1
for i in range(1, 21):
    print(i)

print("\n")

# 2
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
