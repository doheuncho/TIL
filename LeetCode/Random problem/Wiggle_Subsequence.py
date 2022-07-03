# https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return n
        
        prev_diff = nums[1] - nums[0]
        
        result = 2 if prev_diff != 0 else 1
        
        for i in range(2, n):
            cur_diff = nums[i] - nums[i-1]
            if (prev_diff <= 0 and cur_diff > 0) or (prev_diff >= 0 and cur_diff < 0):
                result += 1
                prev_diff = cur_diff
                
        return result
    