# https://leetcode.com/problems/smallest-number-in-infinite-set/

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
class SmallestInfiniteSet:
    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.infinite_set = set(self.heap)
        heapq.heapify(self.heap)
        
    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.heap)
        self.infinite_set.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.infinite_set:
            return
        else:
            heapq.heappush(self.heap, num)
            self.infinite_set.add(num)
            return
        