# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for _ in range(n - 1):
            result = []
            for num in nums:
                last = num % 10
                if last + k <= 9:
                    result.append(num * 10 + last + k)
                if k != 0 and last - k >= 0:
                    result.append(num * 10 + last - k)
            nums = result
        
        return result
                
                    