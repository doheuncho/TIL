# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        stack = [(root, -float(inf))]
        
        while stack:
            node, greatest_value = stack.pop()
            
            if greatest_value <= node.val:
                result += 1
                greatest_value = node.val
            
            if node.left:
                stack.append((node.left, greatest_value))
            if node.right:
                stack.append((node.right, greatest_value))
        
        return result
    