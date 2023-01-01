# https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        for word in words:
            map1 = collections.defaultdict(str)
            map2 = collections.defaultdict(str)
            
            for char1, char2 in zip(word, pattern):
                matched = True
                if char1 not in map1 and char2 not in map2:
                    map1[char1] = char2
                    map2[char2] = char1
                elif map1[char1] == char2 and map2[char2] == char1:
                    continue
                else:
                    matched = False
                    break
            
            if matched:
                result.append(word)
        
        return result
        