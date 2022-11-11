# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        idx = 0

        for num in counter:
            nums[idx] = num
            idx += 1
            
        return len(counter)
    