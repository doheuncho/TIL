# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:        
        if n * k < target:
            return 0
        if n == 1:
            return 1

        modulo =  10 ** 9 + 7
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(i, target +1):
                for k in range(1, k+1):
                    if j - k >= 0:
                        dp[i][j] += dp[i-1][j-k]
                       
        return dp[-1][-1] % modulo
    