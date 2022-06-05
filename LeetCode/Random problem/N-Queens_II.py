# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set() 
        pos_diagonal = set()
        neg_diagonal = set()
        
        return self.solve(n, pos_diagonal, neg_diagonal, col, 0)
        
    def solve(self, n, pos_diagonal, neg_diagonal, col, r):
        result = 0
        
        if r == n:
            return 1
                
        for c in range(n):
            if c in col or r + c in pos_diagonal or r - c in neg_diagonal:
                continue
                
            pos_diagonal.add(r + c)
            neg_diagonal.add(r - c)
            col.add(c)
                
            result += self.solve(n, pos_diagonal, neg_diagonal, col, r + 1)
                
            pos_diagonal.remove(r + c)
            neg_diagonal.remove(r - c)
            col.remove(c)
        
        return result