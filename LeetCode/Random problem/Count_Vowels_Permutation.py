# https://leetcode.com/problems/count-vowels-permutation/

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp[n] = [a, e, i, o, u]
        dp = [[1 for _ in range(5)] for _ in range(n)]
        modulo = 10 ** 9 + 7
        
        for i in range(1, n):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % modulo
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % modulo
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % modulo
            dp[i][3] = (dp[i-1][2]) % modulo
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % modulo
            
        return sum(dp[-1]) % modulo
        