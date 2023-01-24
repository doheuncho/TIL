# https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board = board[::-1]

        for i in range(len(board)):
            if i % 2 == 1:
                board[i] = board[i][::-1]
        
        board = [label for row in board for label in row]
        queue = [(0, 0)]
        visited = set()
        
        while queue:
            cur, steps = queue.pop(0)
            if cur == n ** 2 - 1:
                return steps
            for dice in range(1, 7):
                next = cur + dice
                if next < n ** 2 and next not in visited:
                    visited.add(next)
                    if board[next] == -1:
                        queue.append((next, steps + 1))
                    else:
                        queue.append((board[next] - 1, steps + 1))
        return -1
