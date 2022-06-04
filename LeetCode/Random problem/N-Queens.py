# https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        col = set() 
        pos_diagonal = set()
        neg_diagonal = set()

        board = [["." for _ in range(n)] for _ in range(n)]
        
        def solve(r):
            if r==n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                
            for c in range(n):
                if c in col or r+c in pos_diagonal or r-c in neg_diagonal:
                    continue
                
                pos_diagonal.add(r+c)
                neg_diagonal.add(r-c)
                
                col.add(c)
                
                board[r][c] = "Q"
                
                solve(r+1)
                
                pos_diagonal.remove(r+c)
                neg_diagonal.remove(r-c)
                col.remove(c)
                
                board[r][c] = "."
        
        
        solve(0)
        
        return res