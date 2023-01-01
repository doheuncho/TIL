# https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        prefix = result = 0
        min_avg = float('inf')
        
        for i in range(n):
            prefix += nums[i]
            suffix = total_sum - prefix
            
            if 0 != n - i - 1:
                avg = abs(prefix // (i + 1) - suffix // (n - 1 - i))
            else:
                avg = prefix // (i + 1)
      
            if avg < min_avg:
                min_avg = avg
                result = i
                
        return result
    