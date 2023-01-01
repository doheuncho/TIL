# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        stack = []
        s = '(' + s + ')'
        
        for char in s:
            if char.isdigit():
                result = 10 * result + int(char)
            elif char == '(':
                stack.append((0, '+'))
                result = 0
            elif char != ' ':
                previous, operator = stack.pop()
                if operator == '+':
                    result += previous
                else:
                    result = previous - result
                
                if char == ')':
                    continue
                
                stack.append((result, char))
                result = 0
        
        return result
                