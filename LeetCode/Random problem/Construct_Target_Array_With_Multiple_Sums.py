# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total_sum = sum(target)
        queue = []
        
        for n in target:
            heapq.heappush(queue, -n)
        
        while True:
            n = -heapq.heappop(queue)
            total_sum -= n
            
            if n == 1 or total_sum == 1:
                return True
            if n <= total_sum or total_sum == 0 or n % total_sum == 0:
                return False
            
            n %= total_sum
            total_sum += n
            heapq.heappush(queue, -n)
        