# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for s in strs:
            freqs = Counter(s)
            zeros, ones = freqs['0'], freqs['1']

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(1 + dp[i - zeros][j - ones], dp[i][j])

        return dp[-1][-1]
    