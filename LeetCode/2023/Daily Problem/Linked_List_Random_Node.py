# https://leetcode.com/problems/linked-list-random-node/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.linked_list = []
        while head != None:
            self.linked_list.append(head.val)
            head = head.next
        self.list_len = len(self.linked_list)

    def getRandom(self) -> int:
        return self.linked_list[random.randint(0, self.list_len - 1)]
