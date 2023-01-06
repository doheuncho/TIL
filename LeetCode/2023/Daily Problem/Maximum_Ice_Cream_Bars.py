# https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result = 0

        for cost in sorted(costs):
            if coins >= cost:
                coins -= cost
                result += 1
            else:
                return result
        
        return result
