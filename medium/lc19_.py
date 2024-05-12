# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        visit = []
        start = head

        while start is not None:
            visit.append(start)
            start = start.next

        t = len(visit) - n
        if t == 0 and len(visit) == 1:
            return None
        elif t == 0 and len(visit) > 1:
            return visit[t+1]
        else:
            visit[t-1].next = visit[t].next
            return head

# TestCase
head = ListNode(1, None)
head.next = ListNode(2, None)

A = Solution().removeNthFromEnd(head, 2)
print(A)

