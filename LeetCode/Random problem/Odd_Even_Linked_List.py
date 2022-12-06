# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        result = odd_nodes = head
        even_head = even_nodes = head.next
        result = odd_nodes

        while odd_nodes.next and even_nodes.next:
            odd_nodes.next = odd_nodes.next.next
            odd_nodes = odd_nodes.next
            even_nodes.next = even_nodes.next.next
            even_nodes = even_nodes.next
        
        odd_nodes.next = even_head

        return result
