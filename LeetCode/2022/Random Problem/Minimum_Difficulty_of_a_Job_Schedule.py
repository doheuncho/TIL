# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        
        dp = [[float('inf') for _ in range(d+1)] for _ in range(n)]
        max_diff = jobDifficulty[0]
        
        for i in range(n):
            max_diff = max(max_diff, jobDifficulty[i])
            dp[i][1] = max_diff
            
        for j in range(2, d+1):
            stack = []
            for i in range(j-1, n):
                cur = dp[i-1][j-1]
                while stack and jobDifficulty[stack[-1][0]] <= jobDifficulty[i]:
                    _, min_diff = stack.pop()
                    cur = min(cur, min_diff)
                
                dp[i][j] = min(dp[i][j], jobDifficulty[i] + cur)
                
                if stack:
                    dp[i][j] = min(dp[i][j], dp[stack[-1][0]][j])
                stack.append((i, min(cur, dp[i][j-1])))
        
        return dp[-1][d]
    