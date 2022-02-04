#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    # Write your code here
    answer = 0
    l = 1
    substring_dic = {}
    
    while l < len(s):
        for i in range(len(s)+1-l):
            cur_substring = "".join(sorted(s[i:i+l]))
            if cur_substring in substring_dic:
                substring_dic[cur_substring] += 1
            else:
                substring_dic[cur_substring] = 1
        l += 1
    
    for n in substring_dic.values():
        answer += (n * (n-1)) / 2
        
    return int(answer)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
