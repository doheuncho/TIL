# https://leetcode.com/problems/range-sum-query-mutable/

class NumArray:
    def __init__(self, nums: List[int]):
        self.num_array = nums
        self.total = sum(nums)
        self.half = len(nums) // 2

    def update(self, index: int, val: int) -> None:
        self.total -= self.num_array[index]
        self.num_array[index] = val
        self.total += self.num_array[index]

    def sumRange(self, left: int, right: int) -> int:
        if right - left > self.half:
            out_range = sum(self.num_array[:left] + self.num_array[right+1:])
            return self.total - out_range
        else:
            return sum(self.num_array[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
