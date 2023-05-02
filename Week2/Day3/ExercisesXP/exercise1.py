# 1. Convert the two following lists, into dictionaries.
# Hint: Use the zip method

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = zip(keys, values)


print(dict(result))
