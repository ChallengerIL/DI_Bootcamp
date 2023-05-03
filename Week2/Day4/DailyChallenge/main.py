 # Given a “Matrix” string:
#
#     7i3
#     Tsi
#     h%x
#     i #
#     sM
#     $a
#     #t%
#     ^r!
#
#
# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# A grid means that you could potentially break it into rows and columns, like here:
#
# 7	i	3
# T	s	i
# h	%	x
# i		#
# s	M
# $	a
# #	t	%
# ^	r	!
#
#
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.
#
# Using his technique, try to decode this matrix.
#
# Hints:
# Use
# ● lists for storing data
# ● Loops for going through the data
# ● if/else statements to check the data
# ● String for the output of the secret message
#
# Hint (if needed) : Look at the remote learning “Matrix” videos

import re

MATRIX_STRING = "7i3Tsih%xi #sM $a #t%^r!"
COLUMNS = 3
ROWS = 8

matrix_list = [char for char in MATRIX_STRING]

matrix = [list(row) for row in zip(*[iter(matrix_list)]*COLUMNS)]

no_digits_list = list()

for col in range(COLUMNS):
    for row in range(ROWS):
        if not matrix[row][col].isdigit():
            no_digits_list.append(matrix[row][col])

no_digits_string = "".join(no_digits_list)

print(re.sub('[^A-Za-z0-9]+', ' ', no_digits_string))

# The instructions for this exercise are frustrating.
