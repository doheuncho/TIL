# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        a, b = max(weights), sum(weights)
        
        while a < b:
            mid = (a + b) // 2
            day_need = 1
            cur_weight = 0
            
            for weight in weights:
                cur_weight += weight
                
                if cur_weight > mid:
                    day_need += 1
                    cur_weight = weight
            
            if day_need > days:
                a = mid + 1
            else:
                b = mid
        
        return a        
