# https://leetcode.com/problems/spiral-matrix-ii/

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result = [[-1 for _ in range(n)] for _ in range(n)]
        row = col = d = 0
        num = 1

        while num <= n * n:
            result[row][col] = num
            next_row, next_col = row + direction[d][0], col + direction[d][1]
            if 0 <= next_row < n and 0 <= next_col < n and result[next_row][next_col] == -1:
                row, col = next_row, next_col
            else:
                d = (d + 1) % 4
                row, col = row + direction[d][0], col + direction[d][1]
            num += 1
        
        return result
