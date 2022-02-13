#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def maxSubarray(arr):
    # Write your code here
    dp = [[0] for _ in range(len(arr))]
    dp[0] = arr[0]
    if arr[0] > 0:
        max_sum = arr[0]
    else:
        max_sum = 0
    
    for i in range(1, len(arr)):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
        
        if arr[i] > 0:
            max_sum += arr[i]
    
    if max_sum == 0:
        max_sum = max(arr)
            
    return max(dp), max_sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
