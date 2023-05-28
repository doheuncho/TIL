# https://leetcode.com/problems/paint-house-ii/

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        for i in range(1, len(costs)):
            cost = -1
            m1 = m2 = float('inf')
            
            for j, x in enumerate(costs[i-1]):
                if x < m1:
                    m1, m2 = x, m1
                    cost = j
                elif x < m2:
                    m2 = x
            
            for c in range(len(costs[0])):
                costs[i][c] += m1 if cost != c else m2

        return min(costs[-1])
    