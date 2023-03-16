# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def builder(end: Optional[TreeNode]) -> Optional[TreeNode]:
            if inorder and inorder[-1] != end:
                root = TreeNode(postorder.pop())
                root.right = builder(root.val)
                inorder.pop()
                root.left = builder(end)
                return root
        
        return builder(None)
        