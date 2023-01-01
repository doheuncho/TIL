# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = collections.defaultdict(str)
        seen = []
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = s[i]
            if not dic[char] and word not in seen:
                dic[char] = word
                seen.append(word)
            elif dic[char] != word:
                return False
                        
        return True
