# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        vertical_dic = collections.defaultdict(list)
        result = []
        
        def dfs(node: Optional[TreeNode], row: int, col: int) -> None:
            vertical_dic[col].append((row, node.val))
            
            if node.left:
                dfs(node.left, row+1, col-1)
            if node.right:
                dfs(node.right, row+1, col+1)
        

        dfs(root, 0, 0)
        
        for i in range(min(vertical_dic), max(vertical_dic) + 1):
            cur_nodes = []
            for row, val in sorted(vertical_dic[i]):
                cur_nodes.append(val)
            result.append(cur_nodes)
        
        return result
    