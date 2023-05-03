# 1. Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# 2. The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# 3. Call the function make_shirt().
# 4. Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# 5. Make a large shirt with the default message
# 6. Make medium shirt with the default message
# 7. Make a shirt of any size with a different message.
# 8. Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size: str = "large", message: str = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {message}")


make_shirt()
make_shirt("medium")
make_shirt("small", "I don't like CSS")
make_shirt(size="extra-large", message="I love Israel")
