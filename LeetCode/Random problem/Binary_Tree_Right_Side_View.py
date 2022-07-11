# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        deque = collections.deque()
        if root:
            deque.append(root)
        
        while deque:
            for _ in range(len(deque)):
                node = deque.popleft()
                val = node.val
                
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            
            result.append(val)
        
        return result
    