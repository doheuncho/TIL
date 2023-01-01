# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                pre_day = stack.pop()
                result[pre_day] = day - pre_day
            stack.append(day)
        
        return result
