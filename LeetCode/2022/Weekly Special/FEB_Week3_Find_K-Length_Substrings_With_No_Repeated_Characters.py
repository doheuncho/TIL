# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if k > 26:
            return 0
        count = 0
        
        for i in range(len(s) - k + 1):
            flag =True
            bf = [0 for _ in range(26)]
            for j in range(i, i+k):
                cur = ord(s[j]) - ord('a')
                bf[cur] += 1
                
                if bf[cur] > 1:
                    flag = False
                    break
            if flag:
                count +=1
        
        return count
        