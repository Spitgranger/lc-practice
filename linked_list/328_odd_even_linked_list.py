from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The solution to this problem is to think about how a linked list works. We
# start by initializing two pointers, one called odd assigned to te head and
# another called even assigned to head.next. We then iterate through The
# linked list stoping when even or even.next becomes None as that will be the
# first to reach the end. At each iteration we assign odd.next equal to the next
# odd node, that being of course event.next, and then advance odd by setting it
# equal to odd.next (the next odd node). At the end we are left with two pointers
# to the end of each of each even and odd node list. Since odd nodes come first 
# we set the odd.next equal to the beginning of the even node and return the pointers
# to the head of the odd list. The edge cases would be empty list (return None) or 
# a list of size 1 (return head). This takes O(n) time.
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head.next is None:
            return head
        odd = head
        return_node = odd
        even = head.next
        ret = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = ret
        return return_node
