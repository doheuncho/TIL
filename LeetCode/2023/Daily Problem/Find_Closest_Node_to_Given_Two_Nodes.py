# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distance_from_1, distance_from_2 = [-1] * len(edges), [-1] * len(edges)
        result = -1

        def dfs(node: int, dist: int, distance_array: List[int]):
            if node != -1 and distance_array[node] == -1:
                distance_array[node] = dist
                dfs(edges[node], dist + 1, distance_array)
        
        dfs(node1, 0, distance_from_1)
        dfs(node2, 0, distance_from_2)
        cur_max = float('inf')
        
        
        for i in range(len(distance_from_1)):
            if distance_from_1[i] != -1 and distance_from_2[i] != -1:
                dist = max(distance_from_1[i], distance_from_2[i])
                if dist < cur_max:
                    result = i
                    cur_max = dist
        
        return result
