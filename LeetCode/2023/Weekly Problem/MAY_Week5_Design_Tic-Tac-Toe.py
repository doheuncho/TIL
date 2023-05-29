# https://leetcode.com/problems/design-tic-tac-toe/

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag_1 = 0
        self.diag_2 = 0

    def move(self, row: int, col: int, player: int) -> int:      
        if player == 1:
            self.row[row] += 1
            self.col[col] += 1
            if row + col + 1== self.n:
                self.diag_1 += 1
            if row == col:
                self.diag_2 += 1
        else:
            self.row[row] -= 1
            self.col[col] -= 1
            if row + col + 1== self.n:
                self.diag_1 -= 1
            if row == col:
                self.diag_2 -= 1
        
        check_list = [abs(self.row[row]), abs(self.col[col]), abs(self.diag_1), abs(self.diag_2)]
        if self.n in check_list:
            return player
        
        return 0
