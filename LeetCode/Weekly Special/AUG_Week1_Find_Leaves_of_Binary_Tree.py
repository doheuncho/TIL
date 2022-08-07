# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = collections.defaultdict(list)
        
        def dfs(node, level):
            if not node:
                return level
            left = dfs(node.left, level)
            right = dfs(node.right, level)
            level = max(left, right)
            result[level].append(node.val)
            return level + 1
        
        dfs(root, 0)
        
        return result.values()
    