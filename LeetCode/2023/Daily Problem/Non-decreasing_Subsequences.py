# https://leetcode.com/problems/non-decreasing-subsequences/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)        
        subsequences = set()

        def dfs(idx: int, arr: List[int]) -> None:
            for i in range(idx, n):
                if arr[-1] <= nums[i]:
                    subsequences.add((*arr, nums[i]))
                    dfs(i+1, [*arr, nums[i]])
                dfs(i+1, [nums[i]])
        

        dfs(1, [nums[0]])
               
        return [i for i in subsequences]
