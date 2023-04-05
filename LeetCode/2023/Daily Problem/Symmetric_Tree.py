# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(node_1, node_2):
            if not node_1 and not node_2:
                return True
            if not node_1 or not node_2:
                return False
            return node_1.val == node_2.val and helper(node_1.left, node_2.right) and helper(node_1.right, node_2.left)
        
        return helper(root, root)
    