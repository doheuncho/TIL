# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = sum(data)
        cur_window = max_window = sum(data[:n])
        
        for i in range(len(data) - n):
            cur_window += (-data[i] + data[i + n])
            max_window = max(max_window, cur_window)
        
        return n - max_window
    