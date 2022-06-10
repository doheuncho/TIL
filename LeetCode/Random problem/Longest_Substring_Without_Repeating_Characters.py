# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = left = 0
        mp = {}

        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]], left)

            max_length = max(max_length, right - left + 1)
            mp[s[right]] = right + 1

        return max_length
    