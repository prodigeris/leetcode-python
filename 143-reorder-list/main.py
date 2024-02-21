import collections
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        o = collections.deque()
        e = collections.deque()
        i = 0
        while head:
            if i % 2 == 0:
                e.append(head)
            else:
                o.append(head)
            head = head.next
            i += 1
        while o or e:
            

h5 = ListNode(5)
h4 = ListNode(4, next=h5)
h3 = ListNode(3, next=h4)
h2 = ListNode(2, next=h3)
h1 = ListNode(1, next=h2)

Solution().reorderList(h1)

print("Atsakymas")
while h1 is not None:
    print(h1.val)
    h1 = h1.next
