from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # The idea is to notice that reversing the second half of the linked list gives us a way to iterate through each pair in the list. Therefore
    # all we have to do is use slow and fast pointer to find the middle, reverse the second half and then iterate through each half of the list,
    # getting the maximum pair sum every time. This takes O(n) time.
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        start = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow:
            prev_node = slow.next
            slow.next = prev
            prev = slow
            slow = prev_node
        max_sum = 0
        while prev:
            max_sum = max(max_sum, prev.val + start.val)
            prev = prev.next
            start = start.next
        return max_sum
