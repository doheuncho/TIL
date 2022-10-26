# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # remainders = {sub sum remainder : last index of sub array)
        remainders = {0: -1}
        sub_sum = 0
        
        for i in range(len(nums)):
            sub_sum += nums[i]
            remainder = sub_sum % k
            
            if remainder not in remainders:
                remainders[remainder] = i
            elif i - remainders[remainder] > 1:
                return True
        
        return False
