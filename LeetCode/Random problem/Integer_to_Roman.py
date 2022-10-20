# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dic = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C",
                    90: "XC", 50: "L", 40: "XL", 10: "X",
                    9: "IX", 5: "V", 4: "IV", 1: "I"}
        result = ""
        
        while num:
            for value in roman_dic:
                count, num = divmod(num, value)
                for _ in range(count):
                    result += roman_dic[value]
        
        return result
    