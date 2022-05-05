# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        x = 0
        
        while x < len(nums) and nums[x] > x:
            x += 1
        
        if x < len(nums) and x == nums[x]:
            return -1
        else:
            return x
        