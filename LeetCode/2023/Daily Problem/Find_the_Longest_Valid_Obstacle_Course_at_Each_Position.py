# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        stack, result = [], []
        
        for obstacle in obstacles:
            idx = bisect.bisect_right(stack, obstacle)
            if idx == len(stack):
                stack.append(obstacle)
            else:
                stack[idx] = obstacle
            result.append(idx+1)
            
        return result
    