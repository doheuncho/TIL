# https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = collections.defaultdict(int)
        ids = {}
        result = []

        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            seq = (dfs(root.left), root.val, dfs(root.right))
            if seq not in ids:
                ids[seq] = len(ids) + 1
            
            id = ids[seq]
            count[id] +=1
            if count[id] == 2:
                result.append(root)

            return id
        
        dfs(root)
        return result
    