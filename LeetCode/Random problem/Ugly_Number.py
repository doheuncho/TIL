# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        ugly_factors = [2, 3, 5]

        if n == 1 or n in ugly_factors:
            return True
        
        for factor in ugly_factors:
            if n % factor == 0:
                return self.isUgly(n // factor)
        
        return False
