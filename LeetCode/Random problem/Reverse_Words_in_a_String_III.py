# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        s = s.split()
        
        for word in s:
            result += word[::-1]
            result += ' '
        
        return result[:-1]
        