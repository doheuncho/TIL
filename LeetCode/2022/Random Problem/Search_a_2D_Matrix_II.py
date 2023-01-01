# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        row, col = len(matrix), len(matrix[0])
        cur_row, cur_col = row - 1, 0
        
        while cur_col < col and cur_row >= 0:
            if matrix[cur_row][cur_col] < target:
                cur_col += 1
            elif matrix[cur_row][cur_col] > target:
                cur_row -= 1
            else:
                return True
        
        return False
