# https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        result = 1
        seen = set()

        for char in s:
            if char in seen:
                result += 1
                seen = set()
            seen.add(char)
        
        return result
