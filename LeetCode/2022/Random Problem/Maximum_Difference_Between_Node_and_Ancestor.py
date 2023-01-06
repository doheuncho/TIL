# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode], cur_max: int, cur_min: int) -> int:
            if not node:
                return cur_max - cur_min

            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            left = dfs(node.left, cur_max, cur_min)
            right = dfs(node.right, cur_max, cur_min)

            return max(left, right)

        return dfs(root, root.val, root.val)