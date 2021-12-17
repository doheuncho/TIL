# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
# 메모리 : 14.4 MB
# 시간 : 47 ms
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 뒤집기
        matrix.reverse()
        # 전치
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
