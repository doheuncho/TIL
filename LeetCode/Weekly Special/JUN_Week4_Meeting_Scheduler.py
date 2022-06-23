# https://leetcode.com/problems/meeting-scheduler/

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        heap = list(filter(lambda x: x[1] - x[0] >= duration, slots1 + slots2))
        heapq.heapify(heap)

        while len(heap) > 1:
            _, end1 = heapq.heappop(heap)
            start2, _ = heap[0]
            
            if end1 >= start2 + duration:
                return [start2, start2 + duration]
        
        return []
    