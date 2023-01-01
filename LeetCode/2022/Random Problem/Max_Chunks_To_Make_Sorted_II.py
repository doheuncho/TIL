# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        leftmax = [arr[0]] * n
        rightmin = [arr[-1]] * n
        chunk = 1
        
        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], arr[i])
            rightmin[-1-i] = min(rightmin[-i], arr[-i-1])
        
        
        
        for i in range(n-1):
            if leftmax[i] <= rightmin[i+1]:
                chunk += 1
        
        return chunk
