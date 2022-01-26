#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    count_char = {}
    for char in s:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1
    
    check_dic = {}
    
    for item in count_char:
        if count_char[item] in check_dic:
            check_dic[count_char[item]] += 1
        else:
            check_dic[count_char[item]] = 1
       
    if len(check_dic) == 1:
        return('YES')
    if len(check_dic) > 2:
        return('NO')
    if len(check_dic) == 2:
        if check_dic[max(check_dic)] == 1 and max(check_dic) - min(check_dic) == 1:
            return('YES')
        elif check_dic[min(check_dic)] == 1:
            return('YES')
        else:
            return('NO')

            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
