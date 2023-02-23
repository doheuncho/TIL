# https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n, i = len(profits), 0

        projects = sorted(list(zip(capital, profits)))
        q = []
        
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(q, -projects[i][1])
                i += 1
            if not q:
                break
            w += -heapq.heappop(q)

        return w
        