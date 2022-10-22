# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        counter = collections.Counter(t)
        start_of_result = end_of_result = left = right = 0
        missing = len(t)
        
        while right < len(s):
            if counter[s[right]] > 0:
                missing -= 1
            counter[s[right]] -= 1
            right += 1
            
            while missing == 0:
                if not end_of_result or end_of_result - start_of_result >= right - left:
                    start_of_result, end_of_result = left, right
                
                if counter[s[left]] >= 0:
                    missing += 1
                counter[s[left]] += 1
                left += 1
        
        return s[start_of_result:end_of_result]
    