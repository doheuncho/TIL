# https://leetcode.com/problems/mirror-reflection/
 
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = math.lcm(p, q)
        
        if (lcm / p) % 2 == 1 and (lcm / q) % 2 == 1:
            return 1
        elif  (lcm / p) % 2 == 0 and (lcm / q) % 2 == 1:
            return 0
        else:
            return 2
        