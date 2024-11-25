# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None
        #1 2 3 4 5
        while node:
            next = node.next #next : 2345
            node.next = prev #node : 1->none

            prev = node

            node = next
        return prev
