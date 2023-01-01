# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = cur = 0

        while cur <= reachable:
            reachable = max(reachable, cur + nums[cur])
            if reachable >= len(nums) - cur:
                return True
            cur += 1
        
        return False
