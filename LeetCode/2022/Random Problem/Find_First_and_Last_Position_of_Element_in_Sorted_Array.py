# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        
        return [start, end]
    