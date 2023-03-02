# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        start, count = 0, 1

        for end in range(1, len(chars)+1):
            if end < len(chars) and chars[end] == chars[end-1]:
                count += 1
            else:
                chars[start] = chars[end-1]
                start += 1
                if count > 1:
                    for d in str(count):
                        chars[start] = d
                        start += 1
                    count = 1
        chars = chars[:start]

        return start
