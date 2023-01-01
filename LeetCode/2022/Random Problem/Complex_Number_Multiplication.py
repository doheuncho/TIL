# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, img1 = map(int, num1[:-1].split('+'))
        real2, img2 = map(int, num2[:-1].split('+'))
        
        return f'{real1 * real2 - img1 * img2}+{real1 * img2 + real2 * img1}i'
    