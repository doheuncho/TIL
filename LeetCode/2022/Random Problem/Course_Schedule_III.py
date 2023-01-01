# https://leetcode.com/problems/course-schedule-iii/

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        queue = []
        date = 0
        
        for duration, lastday in courses:
            heapq.heappush(queue, -duration)
            date += duration
            
            if date > lastday:
                date += heapq.heappop(queue)
        
        return len(queue)
            