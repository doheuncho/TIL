# https://leetcode.com/problems/snapshot-array/

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = [{self.snap_id: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.arr[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.arr[index]:
            return self.arr[index][snap_id]
        else:
            history = list(self.arr[index].keys())
            
            left, right = 0, len(history) - 1
            while left <= right:
                mid = (left + right) // 2
                if history[mid] <= snap_id:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return self.arr[index][history[right]]
    