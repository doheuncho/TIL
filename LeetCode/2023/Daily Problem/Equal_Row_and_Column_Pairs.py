# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0
        rows = collections.defaultdict(int)

        for row in grid:
            rows[tuple(row)] += 1
        
        for col in zip(*grid):
            result += rows[col]
        
        return result
    