# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        result = 0
        n, m = len(grid[0]), len(grid)
        row, col = m-1, 0 

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                result += n - col 
                row -= 1 
            else:
                col += 1 

        return result
