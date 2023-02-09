# https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        result = 1
        max_index = steps = nums[0]
        
        for i in range (1, len(nums) - 1):
            steps -= 1
            max_index = max(max_index, nums[i] + i)

            if steps == 0:
                result += 1
                steps = max_index - i

        return result
    