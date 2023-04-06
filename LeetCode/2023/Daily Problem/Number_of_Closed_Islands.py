# https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0
        
        def dfs(row: int, col: int) -> bool:
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False
            if grid[row][col] == 1:
                return True
            grid[row][col] = 1

            left = dfs(row, col-1)
            right = dfs(row, col+1)
            up = dfs(row-1, col)
            down = dfs(row+1, col)

            return left and right and up and down
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and dfs(row, col):
                    result += 1
        
        return result
