#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closestNumbers(arr):
    # Write your code here
    arr.sort()
    result = []
    min_diff = arr[1] - arr[0]
    
    for i in range(1, len(arr)):
        if min_diff > arr[i] - arr[i-1]:
            min_diff = arr[i] - arr[i-1]
            result = []
            result.append(arr[i-1])
            result.append(arr[i])
        elif min_diff == arr[i] - arr[i-1]:
            result.append(arr[i-1])
            result.append(arr[i])
        else:
            continue
    
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
