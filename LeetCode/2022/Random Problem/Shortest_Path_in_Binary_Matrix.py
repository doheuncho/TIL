# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] or grid[-1][-1]:
            return -1
        
        directions = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        visited = set((0, 0))
        
        queue = collections.deque([(0, 0, 1)])
        
        while queue:
            cur_x, cur_y, length = queue.popleft()
            if cur_x == n-1 and cur_y == n-1:
                return length
            
            for dx, dy in directions:
                x, y = cur_x + dx, cur_y + dy
                if 0 <= x < n and 0 <= y < n:
                    if (x, y) not in visited and grid[x][y] == 0:
                        visited.add((x, y))
                        queue.append((x, y, length + 1))
        
        return -1
    