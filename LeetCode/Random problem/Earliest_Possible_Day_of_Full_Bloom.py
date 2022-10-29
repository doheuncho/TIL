# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        cur_time = result = 0
        
        for i in sorted(range(len(plantTime)), key=lambda x: -growTime[x]):
            cur_time += plantTime[i]
            result = max(result, cur_time + growTime[i])
            
        return result
