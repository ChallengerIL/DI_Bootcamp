# 1. Recap – What is a float? What is the difference between an integer and a float?
# 2. Can you think of another way to generate a sequence of floats?
# 3. Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# 1. Integers are numbers without decimal points. Floats are numbers with decimal points.

import numpy as np

# Numpy solution
first_sequence = list(np.arange(1.5, 5.5, .5))
print(first_sequence)

# List solution
second_sequence = [x / 2 for x in range(3, 11)]
print(second_sequence)
