# https://leetcode.com/problems/number-of-islands-ii/

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result, main, land = [], {}, {}
        for i, j in positions:
            p = (i, j)
            main[p], land[p] = p, [p]
            for q in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if q in main:
                    p, q = main[p], main[q]
                    if p != q:
                        if len(land[p]) < len(land[q]):
                            p, q = q, p
                        land[p] += land[q]
                        for l in land.pop(q):
                            main[l] = p
            result.append(len(land))
        return result
    