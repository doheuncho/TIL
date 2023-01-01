# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [0] * len(arr)
        dp[0] = 1 if arr[0]%2 else 0
        
        for i in range(1, len(arr)):
            if arr[i] % 2 == 1:
                dp[i] = i - dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
        
        return sum(dp) % (10 ** 9 + 7)
        