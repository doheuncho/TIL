#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    # Write your code here
    if s.startswith('0'):
        print('NO')
        return
    
    for i in range(1, len(s)//2 + 1):
        start = s[:i]
        s_sliced = s[i:]
        sliced = 0
        
        while s_sliced:
            if sliced == 0:
                next_num = str(int(start) + 1)
                sliced = 1
            else:
                next_num = str(int(next_num) + 1)
                
            if s_sliced[:len(next_num)] == next_num:
                s_sliced = s_sliced[len(next_num):]
            else:
                break
        
        if s_sliced == '':
            print('YES', start)
            return
    
    print('NO')
    return
    
       
if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
