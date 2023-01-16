# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > end:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        result.append(newInterval)

        return result
