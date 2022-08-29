# https://leetcode.com/problems/the-maze-ii/

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        min_distance=[[10 ** 4 for _ in range(len(maze[0]))] for _ in range(len(maze))]
        heap=[]
        heap.append([0, start[0], start[1]])
        min_distance[start[0]][start[1]] = 0
        directions=[(0,1), (0,-1), (1,0), (-1,0)]
        
        while heap:
            cur_dist, start[0], start[1] = heapq.heappop(heap)
            if (start[0], start[1]) == (destination[0], destination[1]):
                return cur_dist
            
            for d in directions:
                distance = 1
                while True:
                    next_row = start[0] + distance * d[0]
                    next_col = start[1] + distance * d[1]
                    if 0 <= next_row < len(maze) and 0 <= next_col < len(maze[0]) and maze[next_row][next_col] == 0:
                        distance += 1
                    else:
                        break

                distance -= 1
                next_row = start[0] + distance * d[0]
                next_col = start[1] + distance * d[1]

                if cur_dist + distance < min_distance[next_row][next_col]:
                    heapq.heappush(heap, [cur_dist + distance, next_row, next_col])
                    min_distance[next_row][next_col] = cur_dist + distance
        
        return -1
            