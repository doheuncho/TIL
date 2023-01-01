# https://leetcode.com/problems/diagonal-traverse-ii/

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag_nums = max([i+len(nums[i]) for i in range(len(nums))])
        
        result = [[] for _ in range(diag_nums)]

        for i, r in enumerate(nums):
            for j, a in enumerate(r):
                result[i + j].append(a)
        
        return [a for r in result for a in reversed(r)]
