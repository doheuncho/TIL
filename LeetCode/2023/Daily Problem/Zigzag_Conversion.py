# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        result = ""
        n, len_of_pattern = len(s), 2 * (numRows - 1)

        for row_idx in range(numRows):
            index = row_idx
            while index < n:
                result += s[index]
                if 0 < row_idx < numRows - 1:
                    second_index = index + len_of_pattern - 2 * row_idx
                    if second_index < n:
                        result += s[second_index]
                index += len_of_pattern
                
        return result
