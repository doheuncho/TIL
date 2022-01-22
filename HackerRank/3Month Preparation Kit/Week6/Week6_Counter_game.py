#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame(n):
    # Write your code here
    turn = 0
    
    while n > 1:
        if math.log2(n) == int(math.log2(n)):
            n = n / 2
        else:
            n -= 2 ** int(math.log2(n))
        turn += 1

    if turn % 2 == 0:
        return "Richard"
    else:
        return "Louise"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
