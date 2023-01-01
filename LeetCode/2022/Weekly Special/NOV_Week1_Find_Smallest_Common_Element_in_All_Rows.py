# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/submissions/

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        row_sets = []
        
        for row in mat:
            row_sets.append(set(row))
            
        intersection = row_sets[0]
        
        for i in range(1, len(row_sets)):
            intersection &= row_sets[i]
        
        if intersection:
            return min(intersection)
        
        return -1
        