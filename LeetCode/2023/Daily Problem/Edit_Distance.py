# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if i==0 or j==0: 
                return i + j
            if word1[i-1]==word2[j-1]: 
                return dp(i-1, j-1)
            return min(dp(i-1, j-1), dp(i, j-1), dp(i-1, j)) + 1
        return dp(len(word1), len(word2))
