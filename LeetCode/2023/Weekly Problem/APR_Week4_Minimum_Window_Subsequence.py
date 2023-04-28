# https://leetcode.com/problems/minimum-window-subsequence/

class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        def find_end(s: int) -> int:
            cur = 0
            while s < len(s1):
                if s1[s] == s2[cur]:
                    cur += 1
                    if cur == len(s2):
                        return s
                s += 1
            
            return
        
        def find_start(e: int) -> int:
            cur = len(s2) - 1
            while cur >= 0:
                if s1[e] == s2[cur]:
                    cur -= 1
                e -= 1
            
            return e+1

        start, min_len = 0, len(s1) + 1
        result = ""
        
        while start < len(s1):
            end = find_end(start)
            if end == None:
                break

            start = find_start(end)
            cur_len = end - start + 1

            if cur_len < min_len:
                min_len = cur_len
                result = s1[start:end+1]
            
            start += 1
        
        return result
