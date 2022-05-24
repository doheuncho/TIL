# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        
        stack = []
        dp = [0] * (len(s) + 1)
    
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                p = stack.pop()
                dp[i+1] = dp[p] + i - p + 1
                
        return max(dp)
    