# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0 for _ in range(n + 1)]

        for i in range(n-1, -1, -1):
            j = min(n, i + questions[i][1] + 1)
            dp[i] = max(dp[i+1], questions[i][0] + dp[j])
        
        return dp[0]
