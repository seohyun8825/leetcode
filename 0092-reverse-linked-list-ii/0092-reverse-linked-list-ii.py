# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        #0 1 2 3 4 5
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next
        #prev 1
        reverse_start = prev.next
        current = reverse_start.next
        #current 2   0 1 2 3 4 5
        for _ in range(right-left):
            reverse_start.next = current.next
            current.next = prev.next
            prev.next = current
            current = reverse_start.next
        return dummy.next