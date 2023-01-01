# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        dp = [collections.defaultdict(int) for _ in range(n)]
        
        for i in range(n):
            for j in range(0, i):
                delta = nums[i] - nums[j]
                if delta in dp[j]:
                    dp[i][delta] += dp[j][delta] + 1
                    result += dp[j][delta]
                else:
                    dp[i][delta] += 1
        
        return result
    