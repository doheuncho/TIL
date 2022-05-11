# https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_dict = {}
        result = 0
        
        for num in nums:
            if k - num in nums_dict and nums_dict[k - num] != 0:
                result += 1
                nums_dict[k - num] -= 1
            elif num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        return result
    