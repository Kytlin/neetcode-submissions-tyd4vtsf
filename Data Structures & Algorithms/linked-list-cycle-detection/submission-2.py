# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow_ptr, fast_ptr = head, head
        while fast_ptr:
            slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next
            if fast_ptr:
                fast_ptr = fast_ptr.next
            if slow_ptr == fast_ptr:
                return True
        return False