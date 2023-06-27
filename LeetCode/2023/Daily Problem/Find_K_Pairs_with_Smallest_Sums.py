# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result: List[Tuple[int, int]] = []
        heap: List[Tuple[int, int, int]] = []
            
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))

        while heap and len(result) < k:
            _, i, j = heapq.heappop(heap)
            result.append((nums1[i], nums2[j]))
            if i < len(nums1) and j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            if i + 1 < len(nums1) and j == 0:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            
        return result
    