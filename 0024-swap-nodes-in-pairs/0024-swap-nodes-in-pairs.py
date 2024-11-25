# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        while current and current.next:
            current.val, current.next.val = current.next.val, current.val
            current = current.next.next

        return head
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            point = head.next
            head.next = self.swapPairs(point.next)
            point.next = head
            return point
        return head