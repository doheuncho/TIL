# https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = cur_score = left = 0
        dic = defaultdict(int)
        
        for right in range(len(nums)):
            cur = nums[right]
            dic[cur] += 1
            cur_score += cur
            
            while left < right and dic[cur] > 1:
                dic[nums[left]] -= 1
                cur_score -= nums[left]
                left += 1
            
            max_score = max(max_score, cur_score)
        
        return max_score
