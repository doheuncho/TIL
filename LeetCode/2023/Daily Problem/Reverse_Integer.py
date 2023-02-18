# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        
        if x >= 0:
            negative = False
        else:
            negative = True
            x = -x
        
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        
        if negative:
            result *= -1
        
        if -(2**31) <= result <= (2**31 - 1):
            return result
        
        return 0
