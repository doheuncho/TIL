# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = [nums[0]]
        
        for num in nums:
            if num > subsequence[-1]:
                subsequence.append(num)
            else:
                index = bisect.bisect_left(subsequence, num)
                subsequence[index] = num
        
        return len(subsequence)
    