#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#

def prims(n, edges, start):
    # Write your code here
    edges_dic = {}
    in_mst = set([start])
    weight_of_mst = 0
    
    for i in range(1, n+1):
        edges_dic[i] = []
    for x, y, d in edges:
        edges_dic[x] += [[y, d]]
        edges_dic[y] += [[x, d]]

    while len(in_mst) < n:
        min_dist = 10 ** 6
        minnode = -1
        for i in in_mst:
            for j in edges_dic[i]:
                if j[0] not in in_mst:
                    if j[1] < min_dist:
                        min_dist = j[1]
                        minnode = j[0]
        if minnode > 0:
            in_mst.add(minnode)
            weight_of_mst += min_dist
    return weight_of_mst
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + '\n')

    fptr.close()
