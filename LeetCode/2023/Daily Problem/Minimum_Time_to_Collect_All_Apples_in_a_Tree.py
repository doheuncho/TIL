# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(parent: int, node: int) -> int:
            time = 0
            
            for child in graph[node]:
                if child != parent:
                    time += dfs(node, child)

            if (hasApple[node] or time > 0) and node != 0:
                time += 2

            return time

        return dfs(-1, 0)
