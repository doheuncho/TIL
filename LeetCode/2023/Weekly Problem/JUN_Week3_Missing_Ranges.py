# https://leetcode.com/problems/missing-ranges/

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums = [lower - 1] + nums + [upper + 1]
        result = []
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1:
                result.append([nums[i-1] + 1, nums[i] - 1])

        return result
    