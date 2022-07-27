# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        stack = [root]
        prev_node = None
        
        while stack:
            cur_node = stack.pop()
            
            if cur_node:
                stack.append(cur_node.right)
                stack.append(cur_node.left)
                
                if prev_node:
                    prev_node.right = cur_node
                    cur_node.left = None
                    prev_node.left = None
                
                prev_node = cur_node
                    