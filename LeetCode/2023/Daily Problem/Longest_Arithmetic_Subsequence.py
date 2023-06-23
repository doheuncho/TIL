# https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dic = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                diff = nums[i] - nums[j]
                dic[(j, diff)] = dic.get((i, diff), 1) + 1
        
        return max(dic.values())
        