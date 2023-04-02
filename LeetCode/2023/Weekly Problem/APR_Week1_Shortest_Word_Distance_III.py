# https://leetcode.com/problems/shortest-word-distance-iii/

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        result = len(wordsDict)
        idx_1 = idx_2 = -1
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                idx_1 = i
                if idx_2 != -1:
                    result = min(result, idx_1 - idx_2)
            if word == word2:
                idx_2 = i
                if idx_1 != -1 and idx_1 != idx_2:
                    result = min(result, idx_2 - idx_1)
        
        return result
