# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result = 0
        
        for end in range(len(arr)+1):
            for start in range(end):
                if (end - start) % 2:
                    result += sum(arr[start:end])
        
        return result
    