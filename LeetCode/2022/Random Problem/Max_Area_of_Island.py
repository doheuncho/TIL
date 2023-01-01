# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        
        result = 0
        table = [[1 for _ in range(n)] for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] and table[row][col]:
                    cur_area = 0
                    table[row][col] = 0
                    stack = [(row, col)]
                    
                    while stack:
                        row, col = stack.pop()
                        cur_area += 1
                        for n_row, n_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                            if 0 <= n_row < m and 0 <= n_col < n:
                                if grid[n_row][n_col] and table[n_row][n_col]:
                                    stack.append((n_row, n_col))
                                    table[n_row][n_col] = 0
                    
                    result = max(cur_area, result)
        
        return result
