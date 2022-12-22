# https://leetcode.com/problems/sum-of-distances-in-tree/

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # dic[i] = [number of subtree with i'th node, sum of distance between i'th node]
        dic = {i: [1, 0] for i in range(n)}
        
        def dfs(node: int, parent: int) -> None:
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    dic[node][0] += dic[child][0]
                    dic[node][1] += dic[child][0] + dic[child][1]
        
        def dfs2(node: int, parent: int) -> None:
            for child in graph[node]:
                if child != parent:
                    dic[child][1] = dic[node][1] - dic[child][0] + n - dic[child][0]
                    dfs2(child, node)
        
        dfs(0, -1)
        dfs2(0, -1)

        return [dic[i][1] for i in range(n)]
