# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dic = collections.defaultdict(int)
        magazine_dic = collections.Counter(magazine)
        
        for char in ransomNote:
            if char not in magazine_dic:
                return False
            ransomNote_dic[char] += 1
        
        for char in ransomNote:
            if ransomNote_dic[char] > magazine_dic[char]:
                return False
        
        return True
    