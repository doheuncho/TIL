# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = collections.Counter(words)
        seen = set()
        
        result = 0
        has_central = False
        
        for key in counter:
            if key[0] == key[1]:
                if counter[key] % 2 == 1:
                    has_central = True
                result += 2 * (counter[key] // 2)
            elif key not in seen and key[::-1] in counter:
                result += 2 * min(counter[key], counter[key[::-1]])
                seen.add(key)
                seen.add(key[::-1])
        
        if has_central:
            result += 1
        
        result *= 2
            
        return result
