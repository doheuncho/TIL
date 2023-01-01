# https://leetcode.com/problems/convert-to-base-2/

class Solution:
    def baseNeg2(self, n: int) -> str:
        result = ''
        
        if n == 0:
            return '0'
        
        while n != 0:
            r = n % -2
            n = n // -2
            if r < 0:
                n += 1
                r = r + 2
            result = str(r) + result
        
        return result
    