# https://leetcode.com/problems/flip-string-to-monotone-increasing/

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        dp = [0 for _ in range(len(s) + 1)]

        for i in range(len(s)):
            if s[i] == '0':
                dp[i+1] = min(dp[i] + 1, ones)
            else:
                dp[i+1] = dp[i]
                ones += 1
        
        return dp[-1]
