# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        cur_len = 1
        result = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue            
            elif nums[i] == nums[i-1] + 1:
                cur_len += 1
            else:
                result = max(result, cur_len)
                cur_len = 1
        
        result = max(result, cur_len)
        
        return result
    