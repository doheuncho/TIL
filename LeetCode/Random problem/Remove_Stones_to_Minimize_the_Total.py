# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-rocks for rocks in piles]
        heapq.heapify(heap)

        for _ in range(k):
            max_rocks = heapq.heappop(heap)
            heapq.heappush(heap, max_rocks // 2)
        
        return -sum(heap)
