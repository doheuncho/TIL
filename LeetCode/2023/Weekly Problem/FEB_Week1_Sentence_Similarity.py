# https://leetcode.com/problems/sentence-similarity/

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similar_dic = collections.defaultdict(list)

        for x, y in similarPairs:
            similar_dic[x].append(y)
            similar_dic[y].append(x)
        
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i]:
                if sentence2[i] not in similar_dic[sentence1[i]]:
                    return False
        
        return True
