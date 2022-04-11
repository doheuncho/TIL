# https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2, reverse=True)
        result = 0
        
        for i in range(len(nums1)):
            result += nums1[i] * nums2[i]
            
        return result
    
