# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        indegree = [0] * len(colors)
        visited, result = 1, 0

        for u, v in edges:
            graph[u].add(v)
            indegree[v] += 1

        stack = [i for i in range(len(colors)) if indegree[i] == 0]
        counts = {i: collections.defaultdict(int) for i in range(len(colors))}
        
        while stack:
            u = stack.pop()
            counts[u][colors[u]] += 1
            result = max(result, counts[u][colors[u]])
            visited += 1
            for v in graph[u]:
                indegree[v] -= 1
                for i in counts[u]:
                    counts[v][i] = max(counts[u][i], counts[v][i])
                if indegree[v] == 0: 
                    stack.append(v)
        
        if visited == len(graph):
            return -1
        
        return result
    