# https://leetcode.com/problems/minimum-knight-moves/

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(x, y):
            x, y = abs(x), abs(y)
            
            if x + y == 0: # (0, 0)
                return 0
            elif x + y == 2: # (0, 2), (1, 1), (2, 0)
                return 2
            else:
                return min(dfs(x-1, y-2), dfs(x-2, y-1)) + 1
        
        return dfs(x, y)
    