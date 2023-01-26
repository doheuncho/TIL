# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        visited = {}
        heap = [(0, 0, src)]
        adj = collections.defaultdict(list)
        
        for start, end, price in flights:
            adj[start].append((end, price))
        
        while heap:
            cost, stops, node = heapq.heappop(heap)
            if node == dst and stops - 1 <= k:
                return cost
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                for neighbor, price in adj[node]:
                    heapq.heappush(heap, (cost + price, stops + 1, neighbor))
        return -1
