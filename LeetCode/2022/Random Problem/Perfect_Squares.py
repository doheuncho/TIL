# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = [i ** 2 for i in range(1, int(n**0.5)+1)]
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in perfect_squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]
