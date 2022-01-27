#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    # Write your code here    
    ranked_in = []
    
    ranked = sorted(list(set(ranked)), reverse=True)
    idx = len(ranked) - 1
    
    for score in player:
        while idx >= 0 and ranked[idx] <= score:
            idx -= 1
        if idx < 0:
            ranked_in.append(1)
            continue
        ranked_in.append(idx + 2)                
    
    return ranked_in
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
