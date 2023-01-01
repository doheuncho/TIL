# https://leetcode.com/problems/binary-tree-cameras/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        monitored = {None}
        
        def dfs(node, parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
            
                if not parent and node not in monitored:
                    self.result += 1
                    monitored.update({node.left, node.right, node})
                elif node.left not in monitored or node.right not in monitored:
                    self.result += 1
                    monitored.update({node.left, node.right, node, parent})
        
        dfs(root)
        return self.result
