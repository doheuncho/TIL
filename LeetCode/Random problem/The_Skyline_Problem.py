# https://leetcode.com/problems/the-skyline-problem/

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(left, -height, right) for (left, right, height) in buildings]
        events += [(right, 0, 0) for (left, right, height) in buildings]
        events.sort()
        
        result = [[0, 0]]
        heap = [[0, 2**32]]
        
        for left, height, right in events:
            while heap[0][1] <= left:
                heapq.heappop(heap)
            if height:
                heapq.heappush(heap, [height, right])
            if result[-1][1] != -heap[0][0]:
                result.append([left, -heap[0][0]])
               
        return result[1:]
    