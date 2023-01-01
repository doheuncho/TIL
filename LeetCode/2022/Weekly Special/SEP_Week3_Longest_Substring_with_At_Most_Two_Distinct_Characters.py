# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        result = left = right = 0
        substring_dic = collections.defaultdict(int)
        
        while right < len(s):
            cur = s[right]
            substring_dic[cur] += 1
            
            while len(substring_dic) > 2:
                prev = s[left]
                left += 1
                substring_dic[prev] -= 1
                if substring_dic[prev] == 0:
                    del substring_dic[prev]
            result = max(result, right - left + 1)
            right += 1
        
        return result
        