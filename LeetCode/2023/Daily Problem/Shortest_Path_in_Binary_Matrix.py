# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] or grid[-1][-1]:
            return -1
        
        queue = [(0, 0, 1)] # (row, col, dist)
        grid[0][0] = 1

        for row, col, dist in queue:
            if row == col == n-1:
                return dist
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                n_row, n_col = row + dr, col + dc
                if 0 <= n_row < n and 0 <= n_col < n and grid[n_row][n_col] == 0:
                    grid[n_row][n_col] = 1
                    queue.append((n_row, n_col, dist+1))
        
        return -1
