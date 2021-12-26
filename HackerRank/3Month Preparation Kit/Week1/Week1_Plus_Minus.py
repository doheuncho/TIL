#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    integers = len(arr)
    plus = 0
    zero = 0
    minus = 0

    for integer in arr:
        if integer > 0:
            plus += 1
        elif integer < 0:
            minus += 1
        else:
            zero += 1
            
    print(f'{plus/integers:.6f}')
    print(f'{minus/integers:.6f}')
    print(f'{zero/integers:.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
