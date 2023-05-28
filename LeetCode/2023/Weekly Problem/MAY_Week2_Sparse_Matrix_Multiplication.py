# https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        n, m, k = len(mat1), len(mat2[0]), len(mat1[0])
        result = [[0] * m for _ in range(n)]

        for x in range(n):
            for y in range(k):
                if mat1[x][y] == 0:
                    continue
                for z in range(m):
                    result[x][z] += mat1[x][y] * mat2[y][z]

        return result 
