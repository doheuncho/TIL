#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def alternate(s):
    # Write your code here
    ans = 0
    
    for i in range(26):
        for j in range(26):
            if i == j: continue
            
            tmp = 0
            arr = [i,j]
            x = 0
            flg = True
            
            for c in s:
                if c == chr(arr[x] + 97):
                    tmp += 1
                    x ^= 1
                elif c == chr(arr[x^1] + 97):
                    flg = False
                    break
                    
            if tmp > 1 and flg:
                ans = max(ans,tmp)
                print(i,j)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
