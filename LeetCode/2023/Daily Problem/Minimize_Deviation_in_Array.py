# https://leetcode.com/problems/minimize-deviation-in-array/

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = list(set(-(x * 2 if x % 2 == 1 else x) for x in nums))
        heapq.heapify(heap)
        maxi, mini = -heap[0], -max(heap)
        result = maxi - mini

        while heap[0] % 2 == 0:
            x = heapq.heappop(heap)//2
            heapq.heappush(heap, x)
            maxi, mini = -heap[0], min(mini, -x)
            result = min(result, maxi - mini)

        return result
    