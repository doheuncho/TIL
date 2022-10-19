# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter(words)
        heap = []
        result = []
        
        for word, freq in counter.items():
            heapq.heappush(heap, (-freq, word))
        
        for _ in range(k):
            _, word = heapq.heappop(heap)
            result.append(word)
        
        return result
    