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
