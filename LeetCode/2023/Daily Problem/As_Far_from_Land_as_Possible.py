# https://leetcode.com/problems/as-far-from-land-as-possible/
 
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = []
        n = len(grid)
        
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row, col))

        if len(queue) == n ** 2 or len(queue) == 0:
            return -1 
        
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        result = -1

        while queue:
            for _ in range(len(queue)):
                cur_row, cur_col = queue.pop(0)
                for dirs in directions:
                    next_row, next_col = cur_row + dirs[0], cur_col + dirs[1]
                    if n > next_row >= 0 and n > next_col >= 0 and grid[next_row][next_col] == 0:
                        queue.append((next_row, next_col))
                        grid[next_row][next_col] = 1
            result += 1
        
        return result
