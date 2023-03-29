# https://leetcode.com/problems/reducing-dishes/

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        result = cur_satisfaction = 0

        for i in range(len(satisfaction)):
            cur_satisfaction += satisfaction[i]
            if cur_satisfaction < 0:
                break
            result += cur_satisfaction

        return result
