# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for _ in range(n)]
        
        # compare with right child
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1
        
        # compare with left child
        for i in range(n-1, 0, -1):
            if ratings[i] < ratings[i-1]:
                candies[i-1] = max(candies[i-1], candies[i] + 1)
        
        return sum(candies)
    