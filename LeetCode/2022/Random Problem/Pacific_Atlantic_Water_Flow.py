# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return result
        
        m, n = len(heights), len(heights[0])
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def dfs(i: int, j: int, flowalbe: Set[Tuple[int]]) -> None:
            if (i, j) in flowalbe:
                return
            flowalbe.add((i, j))
            for d in direction:
                next_x, next_y = i + d[0], j + d[1]
                if 0 <= next_x < m and 0 <= next_y < n and heights[i][j] <= heights[next_x][next_y]:
                    dfs(next_x, next_y, flowalbe)
        
        pacific = set()
        atlantic = set()
                    
        for row in range(m):
            dfs(row, 0, pacific)
            dfs(row, n - 1, atlantic)
        
        for col in range(n):
            dfs(0, col, pacific)
            dfs(m - 1, col, atlantic)
        
        return list(pacific.intersection(atlantic))
    