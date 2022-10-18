# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        def say(num):
            converted = ""
            right = 0
            
            while right < len(num):
                left = right
                while num[left] == num[right]:
                    right += 1
                    if right == len(num):
                        break
                converted += str(right-left)
                converted += str(num[left])
            
            return converted
        
        result = "1"
        
        for _ in range(n-1):
            result = say(result)
        
        return result
