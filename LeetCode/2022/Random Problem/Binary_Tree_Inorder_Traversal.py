# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            cur_node = stack.pop()
            if cur_node.left:
                temp = cur_node.left
                cur_node.left = None
                stack.extend([cur_node, temp])
            else:
                result.append(cur_node.val)
                if cur_node.right:
                    stack.append(cur_node.right)
        
        return result
