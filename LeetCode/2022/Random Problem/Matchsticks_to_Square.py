# https://leetcode.com/problems/matchsticks-to-square/

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        perimeter = sum(matchsticks)
        
        if perimeter % 4 != 0:
            return False
        
        edge = perimeter / 4
        
        matchsticks.sort(reverse=True)
        
        @cache
        def dfs(e0, e1, e2, e3, i):
            if i >= n:
                return e0 == e1 == e2 == e3 == edge
            
            if e0 > edge or e1 > edge or e2 > edge or e3 > edge:
                return False
            
            possible = False
            
            for side in range(4):
                x = matchsticks[i]
                if side == 0:
                    possible = possible or dfs(e0+x, e1, e2, e3, i+1)
                if side == 1:
                    possible = possible or dfs(e0, e1+x, e2, e3, i+1)
                if side == 2:
                    possible = possible or dfs(e0, e1, e2+x, e3, i+1)
                if side == 3:
                    possible = possible or dfs(e0, e1, e2, e3+x, i+1)
                    
            return possible
        
        return dfs(0, 0, 0, 0, 0)
    