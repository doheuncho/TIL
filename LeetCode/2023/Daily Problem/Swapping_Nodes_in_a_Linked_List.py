# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        from_begin = from_end = cur = head
        dist = 1

        while cur:
            if dist < k:
                from_begin = from_begin.next
            
            if dist > k:
                from_end = from_end.next
            
            cur = cur.next
            dist += 1
        
        temp = from_end.val
        from_end.val = from_begin.val
        from_begin.val = temp

        return head
