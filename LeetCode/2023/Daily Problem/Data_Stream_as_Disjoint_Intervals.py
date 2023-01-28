# https://leetcode.com/problems/data-stream-as-disjoint-intervals/\

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
class SummaryRanges:
    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []

        for num in sorted(self.nums):
            if not intervals or num > intervals[-1][1] + 1:
                intervals.append([num, num])
            elif intervals and num == intervals[-1][1] + 1:
                intervals[-1][1] = num

        return intervals
