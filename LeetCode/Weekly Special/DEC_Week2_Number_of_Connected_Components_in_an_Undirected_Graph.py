# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        result = n - len(graph.keys())

        for node in graph.keys():
            queue = [node]

            if node in visited:
                continue
            
            result += 1

            while queue:
                next_queue = []
                for cur_node in queue:
                    for neighbor in graph[cur_node]:
                        if neighbor in visited:
                            continue
                        visited.add(neighbor)
                        next_queue.append(neighbor)
                
                queue = next_queue
        
        return result
