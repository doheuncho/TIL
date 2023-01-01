# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

class Solution:
    def minDeletions(self, s: str) -> int:
        count_char = collections.Counter(s)
        used_frequency = set()
        result = 0
        
        for char, freq in count_char.items():
            while freq >= 1 and freq in used_frequency:
                freq -= 1
                result += 1
            used_frequency.add(freq)
        
        return result
    