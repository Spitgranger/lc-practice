from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# The idea is just to reverse the linked list in place. Iterate over the linked list, setting the next pointer equal to the previous node
# until we hit the end and then return the last node reversed.


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head != None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
