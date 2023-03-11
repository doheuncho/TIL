# https://leetcode.com/problems/valid-word-square/

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        t = list(map(''.join, itertools.zip_longest(*words, fillvalue="")))
        return t == words
    