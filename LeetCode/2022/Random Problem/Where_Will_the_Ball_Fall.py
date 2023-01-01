# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = [None for _ in range(len(grid[0]))]
        
        for col in range(len(grid[0])):
            ball_num = col
            for row in range(len(grid)):
                next_col = col + grid[row][col]
                if 0 > next_col or next_col > len(grid[0])-1 or grid[row][col] != grid[row][next_col]:
                    result[ball_num] = -1
                    break
                result[ball_num] = next_col
                col = next_col
        
        return result
    