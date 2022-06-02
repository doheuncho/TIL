# https://leetcode.com/problems/transpose-matrix/
 
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        trans = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                trans[i][j] = matrix[j][i]
        
        return trans
    