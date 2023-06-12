# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = end = 0
        n = len(nums)
        result = []
    
        while start < n and end < n:
            if end + 1 < n and nums[end] + 1 == nums[end+1]:
                end = end+1
            else:
                if start == end:
                    result.append(f'{nums[start]}')
                    start =+ 1
                    end =+ 1
                else:
                    result.append(f'{nums[start]}->{nums[end]}')
                    start = end + 1
                    end =+ 1

        return result
    