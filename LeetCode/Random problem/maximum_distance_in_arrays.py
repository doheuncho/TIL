# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        first_min, min_index = min((array[0], i) for i, array in enumerate(arrays))
        first_max, max_index = max((array[-1], i) for i, array in enumerate(arrays))
        
        if min_index != max_index:
            return first_max - first_min
        
        second_min, _ = min((array[0], i) for i, array in enumerate(arrays) if i != min_index)
        second_max, _ = max((array[-1], i) for i, array in enumerate(arrays) if i != max_index)
        
        return max(abs(first_max - second_min), abs(second_max - first_min))
