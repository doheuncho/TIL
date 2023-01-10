# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()
            if node_p and node_q:
                if node_p.val == node_q.val:
                    stack.append((node_p.left, node_q.left))
                    stack.append((node_p.right, node_q.right))
                else:
                    return False
            elif node_p or node_q:
                return False
        
        return True
