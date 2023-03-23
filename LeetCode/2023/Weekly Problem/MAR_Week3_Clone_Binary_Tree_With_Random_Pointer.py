# https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
class Solution:
    def copyRandomBinaryTree(self, root: Optional[Node]) -> Optional[NodeCopy]:
        nodes = {}
    
        def dfs(root: Optional[Node]) -> Optional[NodeCopy]:
            if not root:
                return None
            if root in nodes:
                return nodes[root]
            new_root = NodeCopy(root.val)
            nodes[root] = new_root
            new_root.left = dfs(root.left)
            new_root.right = dfs(root.right)
            new_root.random = dfs(root.random)
            return new_root

        return dfs(root)
