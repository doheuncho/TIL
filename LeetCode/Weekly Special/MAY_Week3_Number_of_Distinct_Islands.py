# https://leetcode.com/problems/number-of-distinct-islands/

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        result = []
        ls = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                steps = ""
                
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    steps = "s" # start
                    ls.append((i, j))
                    
                    while ls:
                        k, l = ls.pop()
                        steps += "b" # back
                        
                        if k+1 < len(grid) and grid[k+1][l] == 1:
                            grid[k+1][l] = 0
                            steps += "d" # down
                            ls.append((k+1, l))
                        if 0 <= k-1 and grid[k-1][l] == 1:
                            grid[k-1][l] = 0
                            steps += "u" # up
                            ls.append((k-1, l))
                        if l+1 < len(grid[0]) and grid[k][l+1] == 1:
                            grid[k][l+1] = 0
                            steps += "r" # right
                            ls.append((k, l+1))
                        if 0 <= l-1 and grid[k][l-1] == 1:
                            grid[k][l-1] = 0
                            steps += "l" # left
                            ls.append((k, l-1))
                            
                    result.append(steps)
                    
        return len(set(result))
        