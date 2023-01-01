# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        
        rootNode = TreeNode(root.val)
        
        if root.children:
            first = root.children[0]
            rootNode.left = self.encode(first)
        
        cur = rootNode.left
        
        for i in range(1, len(root.children)):
            cur.right = self.encode(root.children[i])
            cur = cur.right
        
        return rootNode
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None

        rootNode = Node(data.val, [])

        cur = data.left
        
        while cur:
            rootNode.children.append(self.decode(cur))
            cur = cur.right

        return rootNode
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
