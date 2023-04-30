# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(i: int, roots: List[int]) -> int:
            if i != roots[i]:
                roots[i] = find(roots[i], roots)
            return roots[i]

        def union(u: int, v: int, roots: List[int]) -> int:
            u, v = find(u, roots), find(v, roots)
            if u == v:
                return 0
            roots[u] = v
            return 1


        result = alice_edges = bob_edges = 0
        roots = list(range(n + 1))

        for t, u, v in edges:
            if t == 3:
                if union(u, v, roots):
                    alice_edges += 1
                    bob_edges += 1
                else:
                    result += 1
        roots_copy = roots[:]

        for t, i, j in edges:
            if t == 1:
                if union(i, j, roots_copy):
                    alice_edges += 1
                else:
                    result += 1
        
        for t, i, j in edges:
            if t == 2:
                if union(i, j, roots):
                    bob_edges += 1
                else:
                    result += 1

        return result if alice_edges == bob_edges == n - 1 else -1                
