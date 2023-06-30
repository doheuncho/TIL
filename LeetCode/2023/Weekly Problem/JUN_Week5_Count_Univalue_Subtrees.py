# https://leetcode.com/problems/count-univalue-subtrees/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node: Optional[TreeNode], seen: Set[int]):
            if not node:
                return seen
            left = dfs(node.left, seen)
            right = dfs(node.right, seen)
            seen = left.union(right)
            seen.add(node.val)
            self.result += len(seen) == 1

            return seen

        dfs(root, set())

        return self.result
