# https://leetcode.com/problems/binary-search-tree-iterator-ii/

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.last = root
        self.stack = []
        self.arr = []
        self.pointer = -1

    def hasNext(self) -> bool:
        return self.stack or self.last or self.pointer < len(self.arr)-1

    def next(self) -> int:
        self.pointer += 1
        
        if self.pointer == len(self.arr):
            while self.last:
                self.stack.append(self.last)
                self.last = self.last.left
            cur = self.stack.pop()
            self.last = cur.right
            self.arr.append(cur.val)
        
        return self.arr[self.pointer]

    def hasPrev(self) -> bool:
        return self.pointer > 0        

    def prev(self) -> int:
        self.pointer -= 1
        return self.arr[self.pointer]
