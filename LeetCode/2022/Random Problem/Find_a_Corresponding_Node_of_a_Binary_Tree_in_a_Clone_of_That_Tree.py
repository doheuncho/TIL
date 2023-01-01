# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        origin_queue = deque([original])
        cloned_queue = deque([cloned])

        while origin_queue:
            cur_origin_node = origin_queue.popleft()
            cur_cloned_node = cloned_queue.popleft()
            
            if cur_origin_node is target:
                return cur_cloned_node

            if cur_origin_node:
                origin_queue.append(cur_origin_node.left)
                origin_queue.append(cur_origin_node.right)
                
                cloned_queue.append(cur_cloned_node.left)
                cloned_queue.append(cur_cloned_node.right)
                