# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substring = set()
        
        for i in range(len(s)-k+1):
            cur = s[i:i+k]
            if cur not in substring:
                substring.add(cur)
        
        if len(substring) == 2 ** k:
            return True
        else:
            return False