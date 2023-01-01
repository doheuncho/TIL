# https://leetcode.com/problems/word-search/

class Solution:
    def dfs(self, board: List[List[str]], visited: List[List[bool]], word: str, row: int, col: int) -> bool:
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        if board[row][col] == word[0]:
            if len(word) == 1:
                return True
        else:
            return False
        
        visited[row][col] = True
        
        for direction in directions:
            next_row = row + direction[0]
            next_col = col + direction[1]
            if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                if not visited[next_row][next_col]:
                    if self.dfs(board, visited, word[1:], next_row, next_col):
                        return True
        
        visited[row][col] = False
        return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, visited, word, row, col):
                    return True
                    
        return False
