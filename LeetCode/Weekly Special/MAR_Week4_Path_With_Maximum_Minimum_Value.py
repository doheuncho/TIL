# https://leetcode.com/problems/path-with-maximum-minimum-value/

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        def find_root(x):
            if x != root[x]:
                root[x] = find_root(root[x])
            return root[x]
        
        def union(x, y):
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1
            
        R = len(grid)
        C = len(grid[0])
            
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rank = [1] * (R * C)
        root = list(range(R * C))
            
        visited = [[False] * C for _ in range(R)]
            
        vals = [(row, col) for row in range(R) for col in range(C)]
        vals.sort(key = lambda x: grid[x[0]][x[1]], reverse = True)
            
        for cur_row, cur_col in vals:
            cur_pos = cur_row * C + cur_col
                
            visited[cur_row][cur_col] = True
            for d_row, d_col in dirs:
                new_row = cur_row + d_row
                new_col = cur_col + d_col
                new_pos = new_row * C + new_col
                
                if 0 <= new_row < R and 0 <= new_col < C and visited[new_row][new_col]:
                    union(cur_pos, new_pos)
                        
            if find_root(0) == find_root(R * C - 1):
                return grid[cur_row][cur_col]
            
        return -1
                    