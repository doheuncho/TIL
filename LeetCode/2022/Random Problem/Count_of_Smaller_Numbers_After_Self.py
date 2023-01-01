# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums[::-1]
        nums = [(num, i) for i, num in enumerate(nums)]
        result = [0 for _ in range(n)]
        
        def mergeSort(left, right):
            if left == right:
                return 
            mid = (left + right) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            
            i = left
            
            for j in range(mid + 1, right + 1):
                while i < mid + 1 and nums[i][0] < nums[j][0]:
                    i += 1
                result[nums[j][1]] += i - left
            
            nums[left:right+1] = sorted(nums[left:right+1])
            
        mergeSort(0, len(nums)-1)
        
        return result[::-1]
        