# https://leetcode.com/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        else:
            self.dfs(root, val, depth, 1)
            return root
    
    
    def dfs(self, node: Optional[TreeNode], val: int, depth: int, cur_depth: int) -> None:
        if not node:
            return
        if cur_depth >= depth:
            return
        if cur_depth + 1 == depth:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        
        self.dfs(node.left, val, depth, cur_depth+1)
        self.dfs(node.right, val, depth, cur_depth+1)
        