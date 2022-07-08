# https://leetcode.com/problems/inorder-successor-in-bst-ii/

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
    