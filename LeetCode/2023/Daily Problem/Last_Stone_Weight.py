# https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, x-y)
        
        if not heap:
            return 0
            
        return -heapq.heappop(heap)
