# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        result = 1
        shoot_point = points[0][1]
        
        for  x_start, x_end in points[1:]:
            if x_start > shoot_point:
                result += 1
                shoot_point= x_end
            
        return result
