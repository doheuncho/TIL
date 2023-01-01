# https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        digits = list(str(num))
        
        if "6" in digits:
            digits[digits.index("6")] = "9"
            return int("".join(digits))
        
        return num
    