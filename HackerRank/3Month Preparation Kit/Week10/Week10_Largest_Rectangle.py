#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#


def largestRectangle(h):
    # Write your code here
    stack = []
    max_rec = 0
    
    for idx, height in enumerate(h):
        if not stack:
            stack.append([idx, height])
        else:
            width = idx
            while stack and stack[-1][1] > height:
                value = stack.pop()
                width = value[0]
                max_rec = max(max_rec, value[1] * (idx - value[0]))
            stack.append([width, height])
    for value in stack:
        max_rec = max(max_rec, value[1] * (len(h) - value[0]))
    
    return max_rec


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
