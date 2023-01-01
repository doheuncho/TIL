# https://leetcode.com/problems/best-meeting-point/

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row_idxs = []
        col_idxs = []
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    row_idxs.append(row)
                    col_idxs.append(col)
        
        row_idxs.sort()
        col_idxs.sort()
        num_of_friends = len(row_idxs)
        mid = num_of_friends // 2
        
        return sum([abs(row - row_idxs[mid]) for row in row_idxs]) + sum([abs(col - col_idxs[mid]) for col in col_idxs])
    