# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        median = len(nums) // 2
        
        for num in nums:
            result += abs(nums[median] - num)
        
        return result
    