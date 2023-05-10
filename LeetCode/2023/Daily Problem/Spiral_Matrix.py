# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = [[False for _ in range(n)] for _ in range(m)]
        r = c = d = 0
        result = []

        while len(result) < m * n:
            result.append(matrix[r][c])
            visited[r][c] = True
            nr, nc = r + direction[d][0], c + direction[d][1]
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                r, c = nr, nc
            else:
                d = (d+1) % 4
                r, c = r + direction[d][0], c + direction[d][1]
        
        return result
