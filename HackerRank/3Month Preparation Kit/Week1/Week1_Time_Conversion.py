#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    if s[-2:] == 'PM':
        # 오후 12시는 변경할 필요 없음(마지막 'PM'만 제거)
        if s[:2] == '12':
            return s[:-2]
        hour = str(int(s[:2]) + 12)
        s = hour + s[2:-2]
        return s
    else:
        # 오전 12시는 00시로 변경해야 함
        if s[:2] == '12':
            hour = '00'
            s = hour + s[2:-2]
            return s
        return s[:-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
