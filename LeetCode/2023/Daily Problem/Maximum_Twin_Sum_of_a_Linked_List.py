# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        left = [slow.val]
        result, k = 0, 1

        while fast.next:
            slow = slow.next
            left.append(slow.val)
            fast = fast.next.next
            k += 1

        for i in range(k):
            slow = slow.next
            result = max(result, left[-1 - i] + slow.val)
        
        return result
