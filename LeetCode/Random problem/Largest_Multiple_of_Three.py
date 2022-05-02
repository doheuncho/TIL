# https://leetcode.com/problems/largest-multiple-of-three/

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        dp = [-1, -1, -1]
        
        for digit in digits:
            cur_dp = dp + [0]
            for x in cur_dp:
                y = x * 10 + digit
                dp[y % 3] = max(dp[y % 3], y)
        
        if dp[0] < 0:
            return ""
        
        return str(dp[0])
    