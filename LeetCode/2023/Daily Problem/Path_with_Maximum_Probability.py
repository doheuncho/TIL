# https://leetcode.com/problems/path-with-maximum-probability/


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = [{} for _ in range(n)]

        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            graph[a][b] = prob
            graph[b][a] = prob

        maxheap = []
        probs = [0] * n
        probs[start] = 1
        heapq.heappush(maxheap, (-probs[start], start))

        while maxheap:
            prob, cur = heapq.heappop(maxheap)
            if cur == end:
                return -prob
            for neighbor, n_prob in graph[cur].items():
                if -prob * n_prob > probs[neighbor]:
                    probs[neighbor] = -prob * n_prob
                    heapq.heappush(maxheap, (-probs[neighbor], neighbor))

        return 0
