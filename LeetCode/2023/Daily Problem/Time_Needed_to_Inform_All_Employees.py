# https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for i in range(n)]

        for i, m in enumerate(manager):
            if m >= 0:
                subordinates[m].append(i)
        
        def dfs(i: int) -> int:
            return max([dfs(j) for j in subordinates[i]] or [0]) + informTime[i]
        
        return dfs(headID)
    