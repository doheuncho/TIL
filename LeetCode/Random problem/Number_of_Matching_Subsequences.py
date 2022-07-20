# https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        result = 0
        dic = collections.defaultdict(list)
        
        for i, char in enumerate(s):
            dic[char].append(i)
        
        for word in words:
            cur = -1
            for char in word:
                matched = False
                if char not in dic:
                    break
                else:
                    for i in dic[char]:
                        if i > cur:
                            cur = i
                            matched = True
                            break
                
                if not matched:
                    break
            
            if matched:
                result += 1
        
        return result
    