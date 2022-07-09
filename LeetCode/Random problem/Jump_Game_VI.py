# https://leetcode.com/problems/jump-game-vi/

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        
        queue = deque()
        queue.append(0)
        
        for i in range(1, n):
            while queue and queue[0] + k < i:
                queue.popleft()
            dp[i] = dp[queue[0]] + nums[i]
        
            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        return dp[-1]
    