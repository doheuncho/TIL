# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        queue = collections.deque([0])
        result, seen  = 0, set([0])

        for u, v in connections:
            graph[u].append([v, 1])
            graph[v].append([u, 0])

        while queue:
            city = queue.popleft()
            for neighbor, cost in graph[city]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    result += cost 
                    queue.append(neighbor)
        
        return result
        