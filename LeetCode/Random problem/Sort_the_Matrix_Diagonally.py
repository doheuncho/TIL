# https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def diagonal_sort(x: int, y: int) -> List[int]:
            diag_nums = []
            row = x
            col = y
            
            while row < len(mat) and col < len(mat[0]):
                diag_nums.append(mat[row][col])
                row += 1
                col += 1
            
            diag_nums.sort()
            
            i = 0
            row = x
            col = y
            
            while row < len(mat) and col < len(mat[0]):
                mat[row][col] = diag_nums[i]
                row += 1
                col += 1
                i += 1
            
        for i in range(len(mat)):
            diagonal_sort(i, 0)
            
        for j in range(len(mat[0])):
            diagonal_sort(0, j)
                    
        return mat
