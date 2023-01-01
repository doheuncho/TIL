# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn] = 1
        result = 0
        
        for moves in range(1, maxMove+1):
            temp = [[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        result += dp[i][j]
                    if i == m - 1:
                        result += dp[i][j]
                    if j == 0:
                        result += dp[i][j]
                    if j == n - 1:
                        result += dp[i][j]
                    
                    if i > 0:
                        temp[i][j] += dp[i-1][j] % modulo
                    if i < m - 1:
                        temp[i][j] += dp[i+1][j] % modulo
                    if j > 0:
                        temp[i][j] += dp[i][j-1] % modulo
                    if j < n - 1:
                        temp[i][j] += dp[i][j+1] % modulo
            dp = temp
        
        return result % modulo
    