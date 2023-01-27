# https://leetcode.com/problems/concatenated-words/

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dic = set(words)
        result = []

        for word in words:
            word_len = len(word)
            dp = [False] * (word_len + 1)
            dp[0] = True
            
            for i in range(1, word_len + 1):
                for j in range(1 if i == word_len else 0, i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in dic
            if dp[-1]:
                result.append(word)

        return result
