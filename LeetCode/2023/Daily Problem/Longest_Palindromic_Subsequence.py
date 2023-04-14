# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if s == s[::-1]:
            return len(s)
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for right in range(1, n):
            dp[right][right] = 1
            for left in range(right-1, -1, -1):
                if s[left] == s[right]:
                    dp[left][right] = dp[left+1][right-1] + 2
                else:
                    dp[left][right] = max(dp[left+1][right], dp[left][right-1])
            
        return dp[0][-1]
