# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val,i, node))

        dummy = ListNode()
        current = dummy

        while heap:
            val, idx, node = heappop(heap)  # 가장 작은 값을 가진 노드를 꺼냄
            current.next = node
            current = current.next
            if node.next:  
                heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next     






