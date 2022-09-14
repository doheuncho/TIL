# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        path = {} 
        self.result = 0
        
        def dfs(node: Optional[TreeNode], num_odds: int) -> None:
            if not node:
                return 
            path[node.val] = path.get(node.val, 0) + 1 
            if path[node.val] % 2 == 1:
                num_odds += 1 
            else:
                num_odds -= 1
            if not node.left and not node.right:
                if num_odds <= 1:
                    self.result += 1 
            else:
                dfs(node.left, num_odds) 
                dfs(node.right, num_odds)
            path[node.val] -= 1
        
        dfs(root, 0)
        
        return self.result
    