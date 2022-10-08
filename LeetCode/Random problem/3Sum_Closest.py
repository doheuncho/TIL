# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        
        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                threesum = nums[i] + nums[left] + nums[right]
                cur_diff = abs(target - threesum)
                if diff > cur_diff:
                    diff = cur_diff
                    result = threesum
                if threesum < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                return target
        
        return result
    