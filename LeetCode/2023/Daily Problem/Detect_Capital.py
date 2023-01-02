# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word in [word.upper(), word.lower(), word.capitalize()]:
            return True
            
        return False
