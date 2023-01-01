# https://leetcode.com/problems/remove-interval/

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        
        for start, end in intervals:
            if start > toBeRemoved[1] or end < toBeRemoved[0]:
                result.append([start, end])
            
            else:
                if start < toBeRemoved[0]:
                    result.append([start, toBeRemoved[0]])
                if end > toBeRemoved[1]:
                    result.append([toBeRemoved[1], end])
        
        return result
