# https://leetcode.com/problems/k-inverse-pairs-array/

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [0 for _ in range(k+1)]
        
        for i in range(1, n+1):
            temp = [0 for _ in range(k+1)]
            temp[0] = 1
            
            for j in range(1, k+1):
                if j >= i:
                    temp[j] = (temp[j-1] + dp[j] - dp[j - i]) % modulo
                else:
                    temp[j] = (temp[j-1] + dp[j]) % modulo
            dp = temp
        
        if k == 0:
            return dp[-1] % modulo
        else:
            return (dp[-1] - dp[-2]) % modulo
    