#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    # Write your code here
    result = [[] for i in range(int(max(arr)[0])+1)]
    for i, val in enumerate(arr):
        if i < len(arr) / 2:
            result[int(val[0])].append('-')
        else:
            result[int(val[0])].append(val[1])
    
    print(( ' '.join([' '.join(i) for i in result])).strip())

    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
