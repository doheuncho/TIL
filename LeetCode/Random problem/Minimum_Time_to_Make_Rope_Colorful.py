# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = pre_needed = 0
        
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                pre_needed = 0
            
            if pre_needed < neededTime[i]:
                result += pre_needed
                pre_needed = neededTime[i]
            else:
                result += neededTime[i]
        
        return result
    