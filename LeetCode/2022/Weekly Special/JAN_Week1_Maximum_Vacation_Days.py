# https://leetcode.com/problems/maximum-vacation-days/

class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        num_cities = len(days)
        num_weeks = len(days[0])
        
        connection = [[i for i, connected in enumerate(city) if connected] 
		           for city in flights]
        
        dp = [[0 for _ in range (num_cities)] for _ in range(num_weeks+1)]
        
        for week in range(num_weeks-1, -1, -1):
            for city in range(num_cities):
                stay = days[city][week] + dp[week+1][city]
                move = max((days[other_city][week] + dp[week+1][other_city] for other_city in connection[city]), default=0)
                dp[week][city] = max(stay, move)
        
        return dp[0][0]
    