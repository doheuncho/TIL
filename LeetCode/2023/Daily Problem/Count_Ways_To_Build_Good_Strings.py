# https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[0] = 1
        modulo = 10 ** 9 + 7
        small, big = min(zero, one), max(zero, one)

        for i in range(small, big):
            dp[i] = (dp[i] + dp[i - small]) % modulo
            
        for i in range(big, high + 1):
            dp[i] = (dp[i] + dp[i - small]) % modulo
            dp[i] = (dp[i] + dp[i - big]) % modulo

        result = 0

        for i in range(low, high + 1):
            result = (result + dp[i]) % modulo

        return result
    