# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = -1
        binary_num = bin(num)[2:]
        
        for bit in binary_num:
            if bit == '1':
                result += 2
            else:
                result += 1
        
        return result
                