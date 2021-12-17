# 아래 모듈은 leetcode 에디터에 이미 import 되어있다.
# 메모리 : 14.0 MB
# 시간 : 36 ms
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        # 주어진 행렬을 4분할 하여 그중 한 분할의 셀을 temp에 저장하고 나머지 3개 분할의 셀 3개와 함께 서로 위치를 바꾸어줌.
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                temp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
