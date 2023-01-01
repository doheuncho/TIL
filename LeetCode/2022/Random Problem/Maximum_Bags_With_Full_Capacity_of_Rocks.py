# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        result = 0
        left_capacity = []

        for i in range(n):
            left = capacity[i] - rocks[i]
            if left == 0:
                result += 1
            else:
                left_capacity.append(left)
        
        left_capacity.sort()
        
        for left in left_capacity:
            additionalRocks -= left
            if additionalRocks < 0:
                return result
            else:
                result += 1

        return result
