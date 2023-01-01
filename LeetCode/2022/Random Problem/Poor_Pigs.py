# https://leetcode.com/problems/poor-pigs/

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        case = 1 + minutesToTest // minutesToDie
        result = 0
        
        while 1 < buckets:
            buckets /= case
            result += 1
        
        return result
    