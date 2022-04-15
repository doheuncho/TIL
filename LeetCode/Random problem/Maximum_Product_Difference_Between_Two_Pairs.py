# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1 = min2 = 10000
        max1 = max2 = 0
        
        for n in nums:
            if n <= min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
            
            if n >= max1:
                max1, max2 = n, max1
            elif n > max2:
                max2 = n
        
        return max1 * max2 - min1 * min2
        