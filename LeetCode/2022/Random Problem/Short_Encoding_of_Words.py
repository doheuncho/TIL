# https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        encode = set(words)
        result = 0
        
        for word in words:
            for i in range(1, len(word)):
                encode.discard(word[i:])
        
        for word in encode:
            result += (len(word) + 1)
        
        return result
    