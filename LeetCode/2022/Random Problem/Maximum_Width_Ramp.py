# https://leetcode.com/problems/maximum-width-ramp/

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        table = [(a, i) for i, a in enumerate(nums)]
        table.sort()
        
        width = 0
        min_idx = 50001
        
        for a, i in table:
            width = max(width, i - min_idx)
            min_idx = min(min_idx, i)
            
        return width
    