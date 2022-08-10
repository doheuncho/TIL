# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        queue = deque([(root, 0)])
        result = []
        
        while queue:
            node, order = queue.popleft()
            
            if node:
                dic[order].append(node.val)
                
                queue.append((node.left, order - 1))
                queue.append((node.right, order + 1))
            
        for i in sorted(dic.keys()):
            result.append(dic[i])
        
        return result
    