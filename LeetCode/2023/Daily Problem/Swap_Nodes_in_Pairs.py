# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        result = ListNode()
        first, second = head, result

        while first and first.next:
            second.next = first.next
            first.next = second.next.next
            second.next.next = first
            second = first
            first = first.next
        
        return result.next
