# https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted([(scores[i], ages[i]) for i in range(len(scores))])
        max_age = max(ages)
        dp = [0 for _ in range(max_age + 1)]

        for score, age in players:          
            dp[age] = score + max(max_age + 1)

        return max(dp) 
