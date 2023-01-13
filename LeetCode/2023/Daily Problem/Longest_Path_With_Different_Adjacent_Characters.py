# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        result = 1
        graph = {i: [] for i in range(-1, len(parent))}
        
        for c, p in enumerate(parent):
           graph[p].append(c)
        
        def dfs(node: int) -> int:
            nonlocal result
            first = second = 0
            for child in graph[node]:
                path = dfs(child)
                if s[child] != s[node]:
                    if path > first:
                        second = first
                        first = path
                        
                    elif path > second:
                        second = path
                        
                result = max(result, first + second + 1)
            return first + 1
            
        dfs(0)
        return result
