# https://leetcode.com/problems/max-consecutive-ones-ii/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        result = 0
        cur, prev = 0, -1
        
        for num in nums:
            if num == 1:
                cur += 1
            else:
                prev = cur
                cur = 0
            result = max(result, cur + prev + 1)
        return result
    