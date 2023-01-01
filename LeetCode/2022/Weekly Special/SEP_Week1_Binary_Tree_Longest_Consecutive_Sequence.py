# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], length: int) -> int:
            if node.left:
                if node.val + 1 == node.left.val: 
                    left = dfs(node.left, length+1)
                else:
                    left = dfs(node.left, 1)
            else:
                left = 0
            if node.right:
                if node.val + 1 == node.right.val: 
                    right = dfs(node.right, length+1)
                else:
                    right = dfs(node.right, 1)
            else:
                right = 0
            
            return max(length, left, right)
        
        return dfs(root, 1)
    