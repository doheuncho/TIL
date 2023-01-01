# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node:
                numbers.add(node.val)
                dfs(node.left)
                dfs(node.right)
        
        numbers = set()
        dfs(root)
        
        if len(numbers) < 2:
            return -1
        
        return sorted(numbers)[1]
    