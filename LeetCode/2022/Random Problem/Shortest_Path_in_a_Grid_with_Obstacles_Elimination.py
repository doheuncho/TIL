# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if rows + cols - 2 <= k:
            return rows + cols - 2
        
        queue = deque([(0, 0, 0, k)])
       
        node_dict = {}
        node_dict[(0, 0)] = k

        while queue:
            cur_step, row, col, k = queue.popleft()
            
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]

            if row == rows - 1 and col == cols - 1:
                return cur_step

            for next_row, next_col in neighbors:
                if 0 <= next_row < rows and 0 <= next_col < cols:
                    next_k = k - grid[next_row][next_col]

                    if next_k >= 0 and (next_row, next_col) in node_dict and next_k > node_dict[(next_row, next_col)]:
                        node_dict[(next_row, next_col)] = next_k
                    elif next_k >= 0 and (next_row, next_col) not in node_dict:
                        node_dict[(next_row, next_col)] = next_k
                    else:
                        continue
                    
                    queue.append((cur_step + 1, next_row, next_col, next_k))

        return -1
