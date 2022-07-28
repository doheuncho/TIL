# https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = collections.defaultdict(set)
        visited = set()
        
        for a, b in edges:
            dic[a].add(b)
            
        if len(dic[destination]) != 0:
            return False
        
        def dfs(node):
            if len(dic[node]) == 0:
                return node == destination
            
            for next_node in dic[node]:
                if next_node in visited:
                    return False
                
                visited.add(next_node)
                
                if not dfs(next_node):
                    return False
            
                visited.remove(next_node)
            
            return True
        
        return dfs(source)
