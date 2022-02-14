#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def legoBlocks(n, m):
    # Write your code here
    mod = 10 ** 9 + 7
    dp = [0] * (m + 1)
    dp[0] = 1
    
    for width in range(1, m + 1):
        dp[width] = sum(dp[max(0, width - 4):width])
        dp[width] %= mod
    
    for width in range(m + 1):
        dp[width] = dp[width] ** n
        dp[width] %= mod
    valid = dp[:]
    
    for width in range(len(valid)):
        for separator in range(1, width):
            valid[width] -= valid[separator] * dp[width-separator]
        valid[width] %= mod
    
    return valid[m]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
