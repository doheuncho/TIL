# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        modulo = 10 ** 9 + 7
        left, right = 0, len(nums) - 1
        result = 0
        nums.sort()

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                result += 2 ** (right - left)
                result %= modulo
                left += 1
        
        return result
        