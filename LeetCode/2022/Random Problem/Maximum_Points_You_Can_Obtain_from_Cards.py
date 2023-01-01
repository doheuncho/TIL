# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        untaken = len(cardPoints) - k
        
        cur_sum = min_sum = sum(cardPoints[:untaken])
        
        for i in range(1, k+1):
            cur_sum += (cardPoints[untaken+i-1] - cardPoints[i-1])
            min_sum = min(min_sum, cur_sum)
        
        return sum(cardPoints) - min_sum
        