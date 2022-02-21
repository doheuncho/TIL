#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    result = []
    
    for query in queries:
        sub_max = whole_min = max(arr[:query])
        
        for i in range(query, len(arr)):
            if arr[i-query] == sub_max:
                sub_max = max(arr[i-query+1: i+1])
            elif arr[i] > sub_max:
                sub_max = arr[i]
            
            if whole_min > sub_max:
                whole_min = sub_max
        result.append(whole_min)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
