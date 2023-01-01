# https://leetcode.com/problems/insert-delete-getrandom-o1/

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom() 
 
class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.index:
            last, idx = self.nums[-1], self.index[val]
            self.nums[idx], self.index[last] = last, idx
            self.nums.pop()
            del self.index[val]
            return True
        
        return False
                

    def getRandom(self) -> int:
        return random.choice(self.nums)
