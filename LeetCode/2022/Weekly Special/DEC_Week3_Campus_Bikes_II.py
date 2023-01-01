# https://leetcode.com/problems/campus-bikes-ii/

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def manhattan_dist(worker: List[int], bike: List[int]) -> int:
            return abs(worker[0]-bike[0])+abs(worker[1]-bike[1])

        n, m = len(workers), len(bikes)
        dp = [[float('inf')] * (1 << m) for _ in range(n+1)]
        dp[0][0] = 0

        for i, worker in enumerate(workers):
            for mask in range(1 << m):
                for j, bike in enumerate(bikes):
                    new_mask = mask | (1 << j)
                    if not mask & (1 << j):
                        dp[i+1][new_mask] = min(dp[i+1][new_mask], dp[i][mask] + manhattan_dist(worker, bike))

        return min(dp[-1])
