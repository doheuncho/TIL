# https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node: int, label: int) -> bool:
            labels[node] = label
            
            for dislike in dislike_list[node]:
                if labels[dislike] == labels[node]:
                    return False
                if labels[dislike] == -1 and not dfs(dislike, 1 - label):
                    return False
            
            return True
        
        dislike_list = [[] for _ in range(n + 1)]

        for a, b in dislikes:
            dislike_list[a].append(b)
            dislike_list[b].append(a)
        
        labels = [-1 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if labels[i] == -1 and not dfs(i, 0):
                return False
        
        return True
        