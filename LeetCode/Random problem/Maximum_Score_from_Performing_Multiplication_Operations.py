# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [0 for _ in range(m+1)]
        
        for i in range(1, m+1):
            dp[i] = dp[i-1] + multipliers[i-1] * nums[i-1]
            for left in range(i-1, 0, -1):
                dp[left] = max(dp[left] + multipliers[i-1] * nums[n - i + left],
                               dp[left-1] + multipliers[i-1] * nums[left-1])
            dp[0] = dp[0] + multipliers[i-1] * nums[n-i]
        
        return max(dp)
    