from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# This solution uses a fast pointer that moves at 2x the speed of the slow pointer to find the middle node. Once we have the middle node, we remove it by considering three cases,
# if we have only one node, delete it and return none. the middle node has no value of next, it must be that there are only two nodes, hence set head.next to None. For the third case,
# set the value equal to its next value and set its next value equal to next.next (to become someone, assume their identity and then kill them). This happens in O(n) time.


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        return_node = head
        if not head.next:
            return None
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        if slow.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            return_node.next = None
        return return_node
