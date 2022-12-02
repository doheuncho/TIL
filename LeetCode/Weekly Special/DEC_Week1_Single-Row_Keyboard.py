# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        result = cur_index = 0
        
        for char in word:
            next_indext = keyboard.index(char)
            result += abs(next_indext - cur_index)
            cur_index = next_indext
        
        return result
    