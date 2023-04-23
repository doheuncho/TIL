# https://leetcode.com/problems/restore-the-array/

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        modulo = 10 ** 9 + 7
        n = len(s)
        dp = [1] * (n + 1)

        for end in range(n):
            count = 0
            for start in range(end, max(-1, end - len(str(k))), -1):
                if s[start] == "0":
                    continue
                if int(s[start:end+1]) <= k:
                    count += dp[start]
            if count == 0:
                return 0
        
            dp[end+1] = count % modulo
        
        return dp[-1]
