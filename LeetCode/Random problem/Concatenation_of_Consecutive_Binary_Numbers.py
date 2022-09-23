# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        result = degree = 0
        
        for i in range(1, n+1):
            # if i is power of 2
            if not i & (i - 1):
                degree += 1
            result = (result * (2 ** degree) + i) % modulo
        
        return result
    