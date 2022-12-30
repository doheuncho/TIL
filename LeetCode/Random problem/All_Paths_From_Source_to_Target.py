# https://leetcode.com/problems/all-paths-from-source-to-target/description/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        def pathfinder(cur_node: int) -> List[List[int]]:
            if cur_node == target:
                return [[target]]

            result = []
            for next_node in graph[cur_node]:
                for path in pathfinder(next_node):
                    result.append([cur_node] + path)

            return result

        return pathfinder(0)
