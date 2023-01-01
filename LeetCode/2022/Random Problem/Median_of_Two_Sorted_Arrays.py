# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = (nums1 + nums2)
        nums.sort()
        
        length = len(nums)
        
        if length % 2 == 1:
            return nums[length//2]
        
        return (nums[length//2] + nums[length//2 - 1]) / 2
