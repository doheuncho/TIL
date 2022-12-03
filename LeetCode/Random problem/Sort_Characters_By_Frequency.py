# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        result = ''
        
        for char, freq in counter.most_common():
            result += char * freq
        
        return result
    