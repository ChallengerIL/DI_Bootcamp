# 1. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# 2. Use List Comprehension

input_string = "without,hello,bag,world"
input_list = input_string.split(',')
sorted_list = sorted(input_list)

[print(word, end=",") if word != sorted_list[-1] else print(word) for word in sorted_list]
