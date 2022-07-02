# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        modulo = 10 ** 9 + 7
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        horizontal_length = [horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts)-1)]
        vertical_length = [verticalCuts[i+1] - verticalCuts[i] for i in range(len(verticalCuts)-1)]
        
        result = max(horizontal_length) * max(vertical_length)
        
        return result % modulo
        