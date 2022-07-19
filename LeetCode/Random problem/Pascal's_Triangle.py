# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        
        for row in range(numRows):
            nums = [None for _ in range(row+1)]
            nums[0] = nums[-1] = 1
            
            for i in range(1, row):
                nums[i] = pascal[row-1][i-1] + pascal[row-1][i]
            
            pascal.append(nums)

        return pascal
    