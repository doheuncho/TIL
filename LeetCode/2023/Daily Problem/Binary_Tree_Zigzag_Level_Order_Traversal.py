# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        
        def dfs(node: Optional[TreeNode], level: int) -> None:
            if level >= len(result):
                result.append(collections.deque([node.val]))
            else:
                if level % 2 == 0:
                    result[level].append(node.val)
                else:
                    result[level].appendleft(node.val)

            for next_node in [node.left, node.right]:
                if next_node:
                    dfs(next_node, level+1)

        dfs(root, 0)

        return result
    