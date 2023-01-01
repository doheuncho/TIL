# https://leetcode.com/problems/24-game/

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if not cards:
            return False
        return self.dfs(cards, 4)
        
    
    def dfs(self, cards, n):
        if n == 1:
            if abs(cards[0] - 24) <= 1E-6 :
                return True
        
        for i in range(n):
            for j in range(i + 1, n):
                a, b = cards[i], cards[j]
                cards[j] = cards[n - 1]

                if a != 0:
                    cards[i] = b / a
                    if self.dfs(cards, n - 1):
                        return True
                if b != 0:
                    cards[i] = a / b
                    if self.dfs(cards, n - 1):
                        return True
                
                for temp in [a + b, a - b, b - a, a * b]:
                    cards[i] = temp
                    if self.dfs(cards, n - 1):
                        return True
                
                cards[i], cards[j] = a, b 
        return False
    