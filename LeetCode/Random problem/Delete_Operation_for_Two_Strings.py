# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0 for _ in range(len(word2)+1)]
        
        for i in range(len(word1)+1):
            temp = [0 for _ in range(len(word2)+1)]
            for j in range(len(word2)+1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif word1[i-1] == word2[j-1]:
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = min(dp[j], temp[j - 1]) + 1
            dp = temp
        
        return dp[-1]
    