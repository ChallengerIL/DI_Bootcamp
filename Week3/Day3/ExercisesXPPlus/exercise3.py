# 1. Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
import string
from random import choices

LENGTH = 5


def random_string():
    return ''.join(choices(string.ascii_uppercase + string.ascii_lowercase, k=LENGTH))


if __name__ == '__main__':
    print(random_string())
