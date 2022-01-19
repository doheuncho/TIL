#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#


def misereNim(s):
    # Write your code here
    if max(s) == 1:
        if len(s) % 2 == 0:
            return 'First'
        else:
            return 'Second'
    else:
        # https://en.wikipedia.org/wiki/Nim
        xor = 0
        for n in s:
            xor = xor ^ n
        
        if xor == 0:
            return 'Second'
        else:
            return 'First'
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()
