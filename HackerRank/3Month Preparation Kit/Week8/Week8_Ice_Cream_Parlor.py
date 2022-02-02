#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def icecreamParlor(m, arr):
    # Write your code here
    sorted_by_cost = sorted(range(1, len(arr)+1), key=lambda i: arr[i-1])
    print(sorted_by_cost)
    
    left = 0
    right = len(arr) - 1
    
    while True:
        cur_cost = arr[sorted_by_cost[left]-1] + arr[sorted_by_cost[right]-1]
        
        if cur_cost == m:
            return sorted([sorted_by_cost[left], sorted_by_cost[right]])
        elif cur_cost < m:
            left += 1
        elif cur_cost > m:
            right -= 1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
