# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = collections.defaultdict(int)
        
        for char in s:
            dic[char] += 1
        
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        
        return -1
        