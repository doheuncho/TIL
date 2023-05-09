# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        result = 0

        for i in range(n):
            result += mat[i][i]
            if 2 * i != n-1:
                result += mat[n-1-i][i]
        
        return result
        
