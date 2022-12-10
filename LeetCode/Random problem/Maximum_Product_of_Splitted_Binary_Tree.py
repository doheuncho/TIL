# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sub_sums = []
        modulo = 10 ** 9 + 7

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            sub_sum = node.val + dfs(node.left) + dfs(node.right)
            sub_sums.append(sub_sum)
            return sub_sum
        
        dfs(root)
        total_sum = max(sub_sums)

        return max([(total_sum - sub_sum) * sub_sum for sub_sum in sub_sums]) % modulo
