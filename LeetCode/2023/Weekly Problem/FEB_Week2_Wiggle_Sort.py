# https://leetcode.com/problems/wiggle-sort/

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if (i%2 == 0) == (nums[i] > nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
        return
    