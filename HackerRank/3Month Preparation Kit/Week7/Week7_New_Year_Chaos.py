#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    answer = 0
    personal_switch = {}
    disorderd = True
    
    while disorderd:
        disorderd = False
        for i in range(len(q)-1):
            if q[i] > q[i+1]:
                if q[i] in personal_switch:
                    if personal_switch[q[i]] == 2:
                        print("Too chaotic")
                        return
                    else:
                        personal_switch[q[i]] += 1
                else:
                    personal_switch[q[i]] = 1
                
                q[i], q[i+1] = q[i+1], q[i]
                answer += 1
                disorderd =True
    
    print(answer)
    return


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
