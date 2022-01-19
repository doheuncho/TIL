#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def gamingArray(arr):
    # Write your code here
    cur = int(arr[0])
    maxpoint = 1
    for i in range(1, len(arr)):
        if cur < int(arr[i]):
            cur = int(arr[i])
            maxpoint += 1
    
    if maxpoint % 2 == 0:
        return 'ANDY'
    else:
        return 'BOB'
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
