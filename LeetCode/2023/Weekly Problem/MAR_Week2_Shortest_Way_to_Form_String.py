# https://leetcode.com/problems/shortest-way-to-form-string/

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        cur, result = 0, 1

        for char in target:
            pos = source.find(char, cur)
            if pos == -1:
                cur = 0
                result += 1
                pos = source.find(char, cur)
                if pos == -1:
                    return -1
            cur = pos + 1
        
        return result
    