# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        all_sum = sum(nums)
        
        if all_sum % 2 == 1:
            return False
        else:
            half_sum = all_sum // 2
        
        n = len(nums)
        dp = [[False] * (half_sum + 1) for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(n):
            cur = nums[i]
            for j in range(half_sum+1):
                if j < cur:
                    dp[i+1][j] = dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j] or dp[i][j - cur]
        
        return dp[n][half_sum]
    