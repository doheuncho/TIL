# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        
        for row in matrix:
            for num in row:
                heapq.heappush(heap, -num)
        
        for _ in range(len(heap) - k):
            heapq.heappop(heap)
        
        return -heap[0]
    