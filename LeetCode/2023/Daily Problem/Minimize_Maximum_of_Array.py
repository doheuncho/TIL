# https://leetcode.com/problems/minimize-maximum-of-array/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            result = max(result, (prefix_sum + i) // (i + 1)) # ceiling

        return result
