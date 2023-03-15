# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        i = 0

        while queue[i]:
            queue.append(queue[i].left)
            queue.append(queue[i].right)
            i += 1
        
        for node in queue[i:]:
            if node:
                return False
        
        return True
        