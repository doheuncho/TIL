# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = subarrays = 0
                
        for num in nums:
            if num == 0:
                subarrays += 1
                result += subarrays
            else:
                subarrays = 0
                
        return result
