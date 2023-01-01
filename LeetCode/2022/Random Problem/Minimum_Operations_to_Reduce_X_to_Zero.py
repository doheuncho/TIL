# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left = 0
        cur_sum = sum(nums)
        result = 100001
        
        for right in range(n):
            # cur_sum = sum(nums[:left] + nums[right + 1:])
            cur_sum -= nums[right]
            while cur_sum < x and left <= right:
                cur_sum += nums[left]
                left += 1
            if cur_sum == x:
                result = min(result, left + (n - right - 1))
            
        if result == 100001:
            return -1
        else:
            return result
