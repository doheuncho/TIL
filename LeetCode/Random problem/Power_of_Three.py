# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 2:
            if n % 3 != 0:
                return False
            n /= 3
        if n == 1:
            return True
        return False
            