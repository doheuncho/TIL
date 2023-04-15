# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k+1)

        for pile in piles:
            pile = [*accumulate(pile, initial=0)]
            dp = [max(pile[j] + dp[i-j] for j in range(min(len(pile), i+1))) for i in range(k+1)]
        
        return dp[-1]
    