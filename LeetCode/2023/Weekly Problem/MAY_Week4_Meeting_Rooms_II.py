# https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        heap = []

        for strat, end in intervals:
            if heap and heap[0] <= strat:
                heapq.heappop(heap)
            
            heapq.heappush(heap, end)
            
        return len(heap)
