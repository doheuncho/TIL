# https://leetcode.com/problems/two-sum-bsts/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        nodes_in_root1 = set()
        queue = collections.deque([root1])

        while queue:
            node = queue.popleft()
            nodes_in_root1.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        queue.append(root2)

        while queue:
            node = queue.popleft()
            if target - node.val in nodes_in_root1:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
