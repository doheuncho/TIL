# https://leetcode.com/problems/minimum-absolute-difference/

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = 2000000
        
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                result = []
                min_diff = diff
                result.append([arr[i], arr[i+1]])
            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])
        
        return result
    