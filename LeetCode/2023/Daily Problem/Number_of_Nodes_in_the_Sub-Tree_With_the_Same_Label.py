# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        label_count = [0] * 26
        result = [0] * n
        
        def dfs(parent: int, node: int) -> None:
            label = ord(labels[node]) - ord('a')
            previous = label_count[label]
            label_count[label] += 1
            
            for child in graph[node]:
                if child != parent:
                    dfs(node, child)
                    
            result[node] = label_count[label] - previous
        
        dfs(-1, 0)
        return result
