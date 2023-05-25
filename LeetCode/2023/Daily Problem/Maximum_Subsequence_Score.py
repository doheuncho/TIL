# https://leetcode.com/problems/maximum-subsequence-score/

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        total_sum = 0 
        heap = [] 
       
        nums = [(nums2[i], nums1[i]) for i in range(len(nums1))]
        nums.sort(reverse=True)

        for num2, num1 in nums:
            total_sum += num1
            heapq.heappush(heap, num1)  
           
            if len(heap) == k:
                result = max(result, total_sum * num2) 
                total_sum -= heapq.heappop(heap)
                
        return result
    