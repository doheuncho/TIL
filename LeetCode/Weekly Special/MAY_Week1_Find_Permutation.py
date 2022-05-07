# https://leetcode.com/problems/find-permutation/

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stack, result = [], []
        
        for i in range(len(s)):
            curr_num = i + 1
            stack.append(curr_num)            
            if s[i] == 'I':
                while stack:
                    result.append(stack.pop())
        
        result.append(len(s) + 1)
        while stack:
            result.append(stack.pop())
        
        return result
    