# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        result = []
        
        if m > n:
            return result
        
        s_count = [0] * 26
        p_count = [0] * 26

        for i in range(m):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1
            
        
        if s_count == p_count:
            result.append(0)
        
        for i in range(n - m):
            s_count[ord(s[i]) - ord('a')] -= 1
            s_count[ord(s[i + m]) - ord('a')] += 1

            if s_count == p_count:
                result.append(i + 1)

        return result
    