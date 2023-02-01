# https://leetcode.com/problems/confusing-number-ii/

class Solution:
    def confusingNumberII(self, n: int) -> int:
        dic = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
            }
        result = 0
        
        def dfs(num: int, reverse: int, digits: int) -> None:
            nonlocal result
            if num > n:
                return
            if num != reverse:
                result += 1
            if num > n//10:
                return
            
            for key in dic:
                if digits == 1 and key == 0:
                    continue
                dfs(num*10 + key, reverse + digits*dic[key], digits*10)

        dfs(0, 0, 1)

        return result
