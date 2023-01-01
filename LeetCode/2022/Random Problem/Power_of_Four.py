# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 3:
            if n % 4 != 0:
                return False
            n /= 4
        if n == 1:
            return True
        return False
            