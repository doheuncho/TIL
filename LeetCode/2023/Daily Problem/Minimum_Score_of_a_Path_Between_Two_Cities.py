# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(dict)
        for start, end, distance in roads:
            graph[start][end] = graph[end][start] = distance
        
        result = float('inf')
        visited = set()
        queue = collections.deque([1])

        while queue:
            node = queue.popleft()
            for next_city, distance in graph[node].items():
                if next_city not in visited:
                    queue.append(next_city)
                    visited.add(next_city)
                result = min(result, distance)
                
        return result
    