# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.result = 0
        graph = [[] for _ in range(len(roads) + 1)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(cur_node: int, parent: int) -> int:
            representatives = 1
            for next_node in graph[cur_node]:
                if next_node == parent:
                    continue
                representatives += dfs(next_node, cur_node)
            if cur_node:
                self.result += math.ceil(representatives / seats)
            return representatives
            
        dfs(0, -1)
        return self.result
