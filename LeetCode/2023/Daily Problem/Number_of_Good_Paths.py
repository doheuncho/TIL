# https://leetcode.com/problems/number-of-good-paths/

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        result = n
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        parents = [i for i in range(n)]
        root_counts = [1] * n
        
        def find(x: int) -> int:
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        for a, b in edges:
            parents_a, parents_b = find(a), find(b)
            nums_a, nums_b = root_counts[parents_a], root_counts[parents_b]
            val_a, val_b = vals[parents_a], vals[parents_b]
            if val_a == val_b:
                root_counts[parents_a] += nums_b
                parents[parents_b] = parents_a
                result += nums_a * nums_b
            elif val_a < val_b:
                parents[parents_a] = parents_b
            else:
                parents[parents_b] = parents_a

        return result
