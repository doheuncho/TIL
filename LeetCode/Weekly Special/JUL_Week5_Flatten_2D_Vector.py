# https://leetcode.com/problems/flatten-2d-vector/

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.flatten = []
        for vector in vec:
            for val in vector:
                self.flatten.append(val)
        self.length = len(self.flatten)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.flatten[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < self.length
        