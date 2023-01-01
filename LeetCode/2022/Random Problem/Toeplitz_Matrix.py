# https://leetcode.com/problems/toeplitz-matrix/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        pre_row = []
        for row_idx, row in enumerate(matrix):
            if 0 != row_idx:
                if pre_row != row[1:]:
                    return False
            pre_row = row[:-1]
        return True
        