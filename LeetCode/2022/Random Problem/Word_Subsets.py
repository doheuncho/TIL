# https://leetcode.com/problems/word-subsets/

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        subset_dic = collections.defaultdict(int)
        result = []
        words2 = set(words2)
        
        for word in words2:
            dic = collections.defaultdict(int)
            
            for char in word:
                dic[char] += 1
                
            for char in dic:
                subset_dic[char] = max(subset_dic[char], dic[char])
        
        for word in words1:
            dic = collections.defaultdict(int)
            is_subset = True
            
            for char in word:
                dic[char] += 1
                
            for char in subset_dic:
                if char not in dic or subset_dic[char] > dic[char]:
                    is_subset = False
                    break
            
            if is_subset:
                result.append(word)
                   
        return result
