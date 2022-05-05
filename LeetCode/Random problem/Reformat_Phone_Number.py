# https://leetcode.com/problems/reformat-phone-number/

class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "")
        result = []
        
        for i in range(0, len(number), 3):
            if len(number) - i != 4:
                result.append(number[i:i+3])
            else: 
                result.extend([number[i:i+2], number[i+2:]])
                break 
        
        return "-".join(result)
    