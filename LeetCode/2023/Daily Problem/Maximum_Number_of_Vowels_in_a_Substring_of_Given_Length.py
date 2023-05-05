# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        result = cur = 0

        for i, char in enumerate(s):
            if result == k:
                return result
            
            if i >= k and s[i-k] in vowels:
                cur -= 1
            if char in vowels:
                cur += 1
        
            result = max(result, cur)

        return result
    