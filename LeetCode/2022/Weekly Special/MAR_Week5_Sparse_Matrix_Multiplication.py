# https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat1[0] or not mat2 or not mat2[0]:
            return [[]]
        n, m, k = len(mat1), len(mat2[0]), len(mat1[0])
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for t in range(k):
                    result[i][j] += mat1[i][t] * mat2[t][j]
        return result 
