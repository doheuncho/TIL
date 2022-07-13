# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        if not root:
            return result
        
        cur_level = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            result.append([])
            cur_len = len(queue)
            
            for i in range(cur_len):
                cur_node = queue.popleft()
                result[cur_level].append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            cur_level += 1
        
        return result
    