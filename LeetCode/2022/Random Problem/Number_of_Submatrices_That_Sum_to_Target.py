# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        r, c = len(matrix), len(matrix[0])
        
        sub_sum = [[0 for _ in range(c)] for _ in range(r)]
        
        for i in range(r):
            for j in range(c):
                if i == 0 and j == 0:
                    sub_sum[i][j] = matrix[i][j]
                elif i == 0:
                    sub_sum[i][j] = matrix[i][j] + sub_sum[i][j-1]
                elif j == 0:
                    sub_sum[i][j] = matrix[i][j] + sub_sum[i-1][j]
                else:
                    sub_sum[i][j] = matrix[i][j] + sub_sum[i-1][j] + sub_sum[i][j-1] - sub_sum[i-1][j-1]
        
        result = 0
        
        for left in range(r):
            for right in range(left, r):
                dic = collections.defaultdict(int)
                dic[0] = 1
                
                for col in range(c):
                    if left == 0:
                        cur_sum = sub_sum[right][col]
                    else:
                        cur_sum = sub_sum[right][col] - sub_sum[left-1][col]
                    result += dic[cur_sum - target]
                    dic[cur_sum] += 1
        
        return result
    