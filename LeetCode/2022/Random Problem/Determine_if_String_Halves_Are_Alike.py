# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s) - 1
        left_vowels = right_vowels = 0
        
        while left < right:
            if s[left] in vowels:
                left_vowels += 1
            if s[right] in vowels:
                right_vowels += 1
            
            left += 1
            right -= 1
        
        return left_vowels == right_vowels
        