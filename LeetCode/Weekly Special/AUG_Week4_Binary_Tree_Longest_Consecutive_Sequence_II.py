# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        if not root:
            return 0, 0
        inc = dec = 1
        
        if root.left:
            left_inc, left_dec = self.dfs(root.left)
            if root.val == root.left.val + 1:
                dec = left_dec + 1
            elif root.val == root.left.val - 1:
                inc = left_inc + 1
        
        if root.right:
            right_inc, right_dec = self.dfs(root.right)
            if root.val == root.right.val + 1:
                dec = max(dec, right_dec + 1)
            elif root.val == root.right.val - 1:
                inc = max(inc, right_inc + 1)
        self.result = max(self.result, inc + dec - 1)
        
        return inc, dec
        
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        self.dfs(root)
        return self.result
        