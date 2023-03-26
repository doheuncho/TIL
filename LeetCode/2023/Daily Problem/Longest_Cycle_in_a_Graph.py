# https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        result = -1
        visited = set()

        for node in range(len(edges)):
            distance, cur_node = 0, node
            distances = dict()
            while cur_node not in visited and cur_node != -1:
                distance += 1
                visited.add(cur_node)
                distances[cur_node] = distance
                cur_node = edges[cur_node]
            result = max(result, distance + 1 - distances.get(cur_node, 10**5))

        return result
