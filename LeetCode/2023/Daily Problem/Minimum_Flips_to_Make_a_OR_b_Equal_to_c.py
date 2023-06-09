# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0

        while a or b or c:
            A, B, C = a&1, b&1, c&1
            
            if C:
                if not A and not B:
                    result += 1
            else:
                result += (A+B)
                    
            a >>= 1
            b >>= 1
            c >>= 1
            
        return result
    