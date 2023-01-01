# https://leetcode.com/problems/set-mismatch/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        ss = sum([num**2 for num in nums])
        n = len(nums)
        
        s -= (n * (n+1)) // 2
        ss -= ((2 * n + 1) * (n + 1) * n) // 6
        
        print(s)
        
        repeated_num = (ss + s ** 2) // (2 * s)
        missing_num = repeated_num - s
        
        return [repeated_num, missing_num]
