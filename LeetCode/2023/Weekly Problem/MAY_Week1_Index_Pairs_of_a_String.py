# https://leetcode.com/problems/index-pairs-of-a-string/

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        words = set(words)
        result = []
        for left in range(len(text)):
            for right in range(1, len(text)+1):
                if text[left:right] in words:
                    result.append([left, right-1])
        
        return result
