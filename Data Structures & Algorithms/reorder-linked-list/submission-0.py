# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid_head = slow.next
        slow.next = None

        prev, cur, nxt = None, mid_head, mid_head
        while cur:
            nxt = nxt.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        front_ptr, back_ptr = head, prev
        parity = 1
        while back_ptr:
            if parity:
                front_temp = front_ptr.next
                front_ptr.next = back_ptr
                front_ptr = front_temp
            else:
                back_temp = back_ptr.next
                back_ptr.next = front_ptr
                back_ptr = back_temp
            parity = not parity