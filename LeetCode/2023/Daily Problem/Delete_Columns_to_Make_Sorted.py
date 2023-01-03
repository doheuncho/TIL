# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        
        for col in zip(*strs):
            if list(col) != sorted(col):
                result += 1
        
        return result
