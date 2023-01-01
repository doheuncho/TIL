# https://leetcode.com/problems/split-array-into-consecutive-subsequences/

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        num = nums[0]
        max_num = max(nums)
        
        while num <= max_num:
            count = counter.get(num)
            if not count:
                num += 1
                continue
            
            counter[num] -= 1
            sub_len = 1
            
            for i in range(num+1, max_num+1):
                count = counter.get(i)
                if not count:
                    break 
                
                counter[i] -= 1
                sub_len +=1
                
                if counter[i] >= 1 and counter[i+1] <= counter[i] and sub_len >= 3:
                    break

            if sub_len < 3:
                return False

        return True