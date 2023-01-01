# https://leetcode.com/problems/two-sum-less-than-k/

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()        
        if len(nums) == 1 or nums[0] + nums[1] >= k:
            return -1
        
        result = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] < k:
                result = max(result, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        
        return result
        