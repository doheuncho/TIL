# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        else:
            x = str(x)            
            for i in range(len(x)//2):
                if x[i] != x[-i-1]:
                    return False
        
        return True
