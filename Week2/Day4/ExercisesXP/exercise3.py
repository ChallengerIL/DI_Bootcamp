# 1. Write a function called describe_city() that accepts the city of a city and its country as parameters.
# 2. The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# 3. Give the country parameter a default value.
# 4. Call your function.

def describe_city(city, country="Israel"):
    print(f"{city} is in {country}")


if __name__ == "__main__":
    describe_city("Reykjavik", "Iceland")
