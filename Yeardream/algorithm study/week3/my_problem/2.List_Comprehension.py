# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
# 메모리 : 14.2 MB
# 시간 : 43 ms
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]
