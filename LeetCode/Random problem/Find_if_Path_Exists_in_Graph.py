# https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        edge_dic = collections.defaultdict(list)
        for a, b in edges:
            edge_dic[a].append(b)
            edge_dic[b].append(a)
            
        visited = [False] * n
        
        def dfs(node: int) -> bool:
            if node == destination:
                return True
            if not visited[node]:
                visited[node] = True
                for next_node in edge_dic[node]:
                    if dfs(next_node):
                        return True
            return False
            
        return dfs(source)
