# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                negatives += 1

        if negatives % 2 == 0:
            return 1
        
        return -1
      
