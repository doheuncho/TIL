# https://leetcode.com/problems/minimum-number-of-refueling-stops/

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target, 10**9+1))
        heap = []
        result = cur_position = 0
        
        for position, fuel in stations:
            startFuel -= (position - cur_position)
            while startFuel < 0 and heap:
                startFuel -= heapq.heappop(heap)
                result += 1
            if startFuel < 0:
                return -1
            heapq.heappush(heap, -fuel)
            cur_position = position
        
        return result
    