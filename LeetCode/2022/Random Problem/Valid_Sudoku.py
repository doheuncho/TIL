# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False for _ in range(10)] for _ in range(9)]
        cols = [[False for _ in range(10)] for _ in range(9)]
        squares = [[False for _ in range(10)] for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                else:
                    num = int(num)
                    
                square_idx = (row // 3) * 3 + col // 3
                
                if squares[square_idx][num]:
                    return False
                squares[square_idx][num] = True
                
                if rows[row][num]:
                    return False
                rows[row][num] = True
                
                if cols[col][num]:
                    return False
                cols[col][num] = True
        
        return True                
                