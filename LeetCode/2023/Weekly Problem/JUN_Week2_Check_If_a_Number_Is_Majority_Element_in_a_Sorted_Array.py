# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return (bisect.bisect_right(nums,target) - bisect.bisect_left(nums,target)) > len(nums)//2
    