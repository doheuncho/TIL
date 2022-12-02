# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter_1 = collections.Counter(word1)
        counter_2 = collections.Counter(word2)
        
        return sorted(counter_1.values()) == sorted(counter_2.values()) and sorted(counter_1.keys()) == sorted(counter_2.keys())
