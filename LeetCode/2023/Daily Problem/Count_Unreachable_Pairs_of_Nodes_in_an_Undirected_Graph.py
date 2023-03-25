# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        seen = [False] * n
        nodes = []
        result = 0
        queue = collections.deque([])
        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)        

        for cur_node in range(n):
            if not seen[cur_node]:
                connected = 1
                queue.append(cur_node)
                seen[cur_node] = True
                while queue:
                    x = queue.popleft()
                    for next_node in graph[x]:
                        if not seen[next_node]:
                            connected += 1
                            seen[next_node] = True
                            queue.append(next_node)
                nodes.append(connected)
        
        s = sum(nodes)

        for num in nodes:
            result += num * (s-num)
            s = s - num
        
        return result
