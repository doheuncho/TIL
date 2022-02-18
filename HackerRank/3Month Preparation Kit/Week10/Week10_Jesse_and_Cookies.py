#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    # Write your code here
    heap = []
    for a in A:
        heapq.heappush(heap, a)
    
    count = 0
        
    while heap[0] < k:
        if len(heap) < 2:
            return -1
        
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        heapq.heappush(heap, first+second*2)
        count += 1
    
    return count
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
