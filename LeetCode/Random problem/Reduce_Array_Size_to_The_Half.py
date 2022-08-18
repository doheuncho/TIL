# https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)
        nums = sorted(counter.values())
        removed = result = 0
        
        while removed < len(arr) / 2:
            removed += nums.pop()
            result += 1
                
        return result
    