# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                move = []
                
                for x, y in direction:
                    if 0 <= i+x < m and  0 <= j+y < n and val > matrix[i+x][j+y]:
                        move.append(dfs(i+x, j+y))
                    else:
                        move.append(0)
                
                dp[i][j] = 1 + max(move)
            
            return dp[i][j]
        
        longest_path = []
        
        for i in range(m):
            for j in range(n):
                longest_path.append(dfs(i, j))
                
        return max(longest_path)
    