# https://leetcode.com/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left, right = 0, len(tokens) - 1
        result = 0
        
        while left <= right:
            if tokens[left] <= power:
                result += 1
                power -= tokens[left]
                left += 1
            elif left < right and result > 0:
                result -= 1
                power += tokens[right]
                right -= 1
            else:
                break
        
        return result
    