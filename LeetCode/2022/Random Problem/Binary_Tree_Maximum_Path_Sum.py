# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def pathfinder(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_sum = max(pathfinder(node.left), 0)
            right_sum = max(pathfinder(node.right), 0)

            self.result = max(self.result, node.val + left_sum + right_sum)

            return max(left_sum + node.val, right_sum + node.val)

        self.result = -float('inf')
        pathfinder(root)
    
        return self.result
