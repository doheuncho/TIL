# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix[0])
        m = len(matrix)
        result = -10 ** 6
        
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] = matrix[i][j] + matrix[i][j-1]
            matrix[i].insert(0, 0)
        
        for j1 in range(n):
            for j2 in range(j1, n):
                arr = [0]
                cur_sum = 0
                for i in range(m):
                    cur_sum += matrix[i][j2+1] - matrix[i][j1]
                    index = bisect.bisect_left(arr, cur_sum - k) 
                    if index < len(arr):
                        if arr[index] == cur_sum - k:
                            return k
                        else:
                            result = max(result, cur_sum - arr[index])
                    bisect.insort(arr, cur_sum) 
        
        return result
