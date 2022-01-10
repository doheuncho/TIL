#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    need_add = 0
    number = low = up = special = 1
    
    for word in password:
        if word in numbers:
            number = 0
        elif word in lower_case:
            low = 0
        elif word in  upper_case:
            up = 0
        elif word in special_characters:
            special = 0
    
    if n + (number + low + up + special) < 6:
        return 6-n
    
    return number + low + up + special
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
