# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bought, profit = -50000 ,0

        for price in prices:
            bought = max(bought, profit - price)
            profit = max(profit, bought + price - fee)
        
        return profit
    