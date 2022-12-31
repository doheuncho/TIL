# https://leetcode.com/problems/minimum-cost-to-connect-sticks/

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        result = 0
        
        while len(sticks) >= 2:
            cost = heapq.heappop(sticks) + heapq.heappop(sticks)
            heapq.heappush(sticks, cost)
            result += cost

        return result
