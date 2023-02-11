# https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        
        for a, b in redEdges:
            graph[a].append((b, 'r'))
        for u, v in blueEdges:
            graph[u].append((v, 'b'))
            
        result = [-1 for _ in range(n)]
        result[0] = 0

        queue = collections.deque([(0, 'r', 0), (0, 'b', 0)])
        visited = set()
        
        visited.add((0, 'r'))
        visited.add((0, 'b'))
        
        while queue:
            node, color, dist = queue.popleft()         
            for next_node, next_color in graph[node]:
                if (next_node, next_color) in visited or color == next_color:
                    continue
                if result[next_node] < 0:
                    result[next_node] = dist + 1
                queue.append((next_node, next_color, dist + 1))
                visited.add((next_node, next_color))
                
        return result
    