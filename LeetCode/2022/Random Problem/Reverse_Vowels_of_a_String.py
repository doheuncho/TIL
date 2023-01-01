# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        result = list(s)
        s = list(s)
        vowels_index = []
        
        for idx, char in enumerate(s):
            if char in vowels:
                vowels_index.append(idx)
        
        reversed_index = vowels_index[::-1]
        
        for i in range(len(vowels_index)):
            result[vowels_index[i]] = s[reversed_index[i]]
        
        return "".join(result)
