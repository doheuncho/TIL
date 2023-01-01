# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10 ** 9 + 7
        result = 0
        arr = [-float('inf')] + arr + [-float('inf')]
        stack = []
        
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                prev = stack.pop()
                result += arr[prev] * (i - prev) * (prev - stack[-1])
            stack.append(i)
            
        return result % modulo
    