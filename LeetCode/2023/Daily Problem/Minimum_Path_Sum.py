# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for col in range(1, m):
            grid[0][col] += grid[0][col-1]
        
        for row in range(1, n):
            for col in range(m):
                if col == 0:
                    grid[row][col] += grid[row-1][col]
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        
        return grid[-1][-1]
    