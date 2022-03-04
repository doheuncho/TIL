# https://leetcode.com/problems/clone-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        cur = Node(root.val)
        
        for child in root.children:
            cur.children.append(self.cloneTree(child))
        
        return cur
    