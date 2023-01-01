# https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7
        heap = []
        result = speed_sum = 0
        
        stats = list(zip(efficiency, speed))
        stats.sort(key=lambda x: x[0], reverse=True)
        
        for cur_efficiency, cur_speed in stats:
            heapq.heappush(heap, cur_speed)
            speed_sum += cur_speed 
            
            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)
                
            result = max(result, speed_sum * cur_efficiency)
        
        return result % modulo 
       