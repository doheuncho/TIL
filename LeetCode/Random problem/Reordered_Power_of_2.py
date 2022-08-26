# https://leetcode.com/problems/reordered-power-of-2/

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        counter = collections.Counter(str(n))
        power_of_two = 1
        
        for i in range(31):
            if counter == collections.Counter(str(power_of_two)):
                return True
            power_of_two *= 2
        
        return False
