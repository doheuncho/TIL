# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        decresing = 0
        
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if decresing == 1:
                    return False
                
                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]
                
                decresing += 1
        
        return True
