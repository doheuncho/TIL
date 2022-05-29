# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = defaultdict(int)
        result = 0
        
        for word in words:
            for w in word:
                dic[word] |= 1 << (ord(w) - 97)
        
        for w1, w2 in combinations(dic.keys(), 2):
            if dic[w1] & dic[w2] == 0: 
                result = max(result, len(w1)*len(w2))
                
        return result
    