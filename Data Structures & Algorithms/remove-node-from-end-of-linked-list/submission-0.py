# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        tmp, prev = head, head
        size = 0
        while prev:
            prev = prev.next
            size += 1

        if size == n:
            return head.next

        prev = tmp
        for _ in range(size-n-1):
            prev = prev.next

        prev.next = prev.next.next
        return tmp