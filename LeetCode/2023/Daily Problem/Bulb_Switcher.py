# https://leetcode.com/problems/bulb-switcher/

class Solution:
    def bulbSwitch(self, n: int) -> int:
        result, i = 0, 1
        
        while i ** 2 <= n:
            result += 1
            i += 1
        
        return result
        