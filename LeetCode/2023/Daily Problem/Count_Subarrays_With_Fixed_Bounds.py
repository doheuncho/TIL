# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = left = right = 0
        last_min = last_max = -1
    
        while right < len(nums):
            if not minK <= nums[right] <= maxK: 
                right += 1
                left = right
                last_min = last_max = -1
            else:
                if nums[right] == minK:
                    last_min = right
                if nums[right] == maxK:
                    last_max = right
                
                if last_min != -1 and last_max != -1:
                    result += (min(last_min, last_max) - left) + 1
                right += 1
        
        return result
