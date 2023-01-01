# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda x:(-x[0], x[1]))
        result = 0
        max_defense = 0
        
        for _, defense in properties:
            if defense < max_defense:
                result += 1
            else:
                max_defense = defense
        return result
    