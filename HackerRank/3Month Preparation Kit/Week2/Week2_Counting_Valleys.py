#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    level = 0
    below = False
    
    for step in path:
        if step == 'U':
            level += 1
        elif step == 'D':
            level -= 1
        
        if below is False and level < 0:
            below = True
            valleys += 1
        elif below is True and level >= 0:
            below = False
    
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
