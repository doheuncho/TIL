#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weightedUniformStrings(s, queries):
    # Write your code here
    count = 1
    scores = set([(ord(s[0]) - 96) * count])
    
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            count = 1
        scores.add((ord(s[i]) - 96) * count)
    
    return ["Yes" if q in scores else "No" for q in queries]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
