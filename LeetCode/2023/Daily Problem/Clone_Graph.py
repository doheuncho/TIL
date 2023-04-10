# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return

        dic = {node.val: Node(node.val, [])}
        queue = collections.deque([node])

        while queue:
            cur_node = queue.pop()
            cur_res = dic[cur_node.val]

            for neighbor in cur_node.neighbors:
                if neighbor.val not in dic:
                    queue.append(neighbor)
                    dic[neighbor.val] = Node(neighbor.val, [])
                cur_res.neighbors.append(dic[neighbor.val])
        
        return dic[node.val]
    