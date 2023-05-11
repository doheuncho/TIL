# https://leetcode.com/problems/uncrossed-lines/

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m
        dp = [0] * (n + 1)
        
        for i in range(m):
            for j in range(n-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[j+1] = dp[j] + 1
                
            for j in range(n):
                dp[j+1] = max(dp[j+1], dp[j])
        
        return dp[-1]
