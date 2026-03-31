# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def applyAddtoList(self, l1, l2):
        cur1, cur2 = l1, l2
        carry_over = 0
        while cur1.next:
            val_to_add = 0
            if cur2:
                val_to_add = cur2.val
            cur1.val, carry_over = (cur1.val + val_to_add + carry_over) % 10, (cur1.val + val_to_add + carry_over) // 10
            
            cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        
        val_to_add = 0
        if cur2:
            val_to_add = cur2.val
        cur1.val, carry_over = (cur1.val + val_to_add + carry_over) % 10, (cur1.val + val_to_add + carry_over) // 10

        if carry_over > 0:
            cur1.next = ListNode(carry_over)
        
        return l1

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first, pick list with more digits to iterate on
        len_l1, len_l2 = 0, 0
        cur1, cur2 = l1, l2
        while cur1:
            cur1 = cur1.next
            len_l1 += 1
        while cur2:
            cur2 = cur2.next
            len_l2 += 1

        if len_l1 > len_l2:
            return self.applyAddtoList(l1, l2)
        else:
            return self.applyAddtoList(l2, l1)
