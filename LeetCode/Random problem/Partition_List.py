# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = left_start = ListNode(None)
        right = right_start = ListNode(None)
        node = head
        
        while node:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
        
            node = node.next
        
        left.next, right.next = right_start.next, None
        
        return left_start.next
        