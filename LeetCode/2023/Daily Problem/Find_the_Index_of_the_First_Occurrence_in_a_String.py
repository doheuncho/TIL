# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len, haystack_len = len(needle), len(haystack)

        for i in range(haystack_len - needle_len + 1):
            if needle == haystack[i:i + needle_len]:
                return i

        return -1
    