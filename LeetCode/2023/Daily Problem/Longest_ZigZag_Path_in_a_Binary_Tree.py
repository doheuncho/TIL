# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [(root, 0, None)]

        while stack:
            node, distance, is_right = stack.pop()
            if node:
                result = max(result, distance)
                if is_right:
                    stack.append((node.left, distance+1, False))
                    stack.append((node.right, 1, True))
                else:
                    stack.append((node.left, 1, False))
                    stack.append((node.right, distance+1, True))
        
        return result
