# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        origin_max = max(candies)
        result = []

        for candy in candies:
            if candy + extraCandies >= origin_max:
                result.append(True)
            else:
                result.append(False)
        
        return result
