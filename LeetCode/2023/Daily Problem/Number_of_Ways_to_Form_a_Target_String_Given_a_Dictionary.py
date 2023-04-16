# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n, m = len(words[0]), len(target)
        modulo = 10 ** 9 + 7
        dp = [1] + [0] * (m)
        char_count = [[0] * 26 for _ in range(n)]

        for i in range(n):
            for word in words:
                char_count[i][ord(word[i]) - ord('a')] += 1
        
        for i in range(n):
            for j in range(m-1, -1, -1):
                dp[j+1] += dp[j] * char_count[i][ord(target[j]) - ord('a')]
                dp[j+1] %= modulo

        return dp[m]
