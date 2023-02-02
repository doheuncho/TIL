# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache
        def dp(i):
            if i == 0:
                return 0
            elif i == 1 or i == 2:
                return 1
        
            return dp(i-1) + dp(i-2) + dp(i-3)
        

        return dp(n)