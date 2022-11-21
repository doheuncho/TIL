# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = collections.deque([[0, entrance[0], entrance[1]]])
        maze[entrance[0]][entrance[1]] = "+"
        
        while queue:
            distance, row, col = queue.popleft()
            
            for direction in directions:
                next_row, next_col = row + direction[0], col + direction[1]
                
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":
                    if next_row * next_col == 0 or next_row == rows - 1 or next_col == cols - 1:
                        return distance + 1
                    
                    maze[next_row][next_col] = "+"
                    queue.append([distance + 1, next_row, next_col])
        
        return -1
    