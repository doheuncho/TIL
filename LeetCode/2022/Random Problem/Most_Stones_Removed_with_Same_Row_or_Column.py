# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:        
        points = set((i, j) for i, j in stones)
        island = 0
        rows, cols = collections.defaultdict(list), collections.defaultdict(list)
        
        def dfs(i: int, j: int) -> None:
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)
        
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island
