# https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0

        def dfs(row: int, col: int) -> None:
            if row == -1 or col == -1 or row == rows or col == cols or grid[row][col] == 0:
                return

            grid[row][col] = 0

            dfs(row, col-1)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row+1, col)

            return

        for row in range(rows):
            for col in range(cols):
                if (row == 0 or col == 0 or row == rows - 1 or col == cols - 1) and grid[row][col] == 1:
                    dfs(row, col)

        for row in range(rows):
            result += sum(grid[row])

        return result
    