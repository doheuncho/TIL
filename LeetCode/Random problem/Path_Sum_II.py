# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if root.val == targetSum and not root.left and not root.right:
            return [[root.val]]
        
        result = []
        stack = [(root, [root.val])]
        
        while stack:
            cur_node, cur_path = stack.pop()
            remain = targetSum - sum(cur_path)
            left_child, right_child = cur_node.left, cur_node.right
            
            if left_child:
                left_path = cur_path + [left_child.val]
                if left_child.val == remain and not left_child.left and not left_child.right:
                    result.append(left_path)
                stack.append((left_child, left_path))
            
            if right_child:
                right_path = cur_path + [right_child.val]
                if right_child.val == remain and not right_child.left and not right_child.right:
                    result.append(right_path)
                stack.append((right_child, right_path))
        
        return result
        