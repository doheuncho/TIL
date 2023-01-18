# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_max = cur_min = all_sum = 0
        max_sum = min_sum = nums[0]

        for num in nums:
            cur_max = max(cur_max, 0) + num
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min, 0) + num
            min_sum = min(cur_min, min_sum)
            all_sum += num
        


        if min_sum == all_sum:
            return max_sum
        else:
            return max(max_sum, all_sum - min_sum)