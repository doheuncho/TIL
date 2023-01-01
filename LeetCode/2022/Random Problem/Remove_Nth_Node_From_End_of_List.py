# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_node = pre_node = head
        length = 1
        
        while cur_node.next:
            length += 1
            cur_node = cur_node.next
            if length > n + 1:
                print(pre_node)
                pre_node = pre_node.next
                
        if length == n:
            return head.next
        else:
            pre_node.next = pre_node.next.next
            return head
        