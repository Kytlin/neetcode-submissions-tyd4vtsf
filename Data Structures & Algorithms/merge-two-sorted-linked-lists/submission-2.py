# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        res_list = None
        p1, p2 = list1, list2
        if list1.val < list2.val:
            res_list = ListNode(list1.val)
            p1 = p1.next
        else:
            res_list = ListNode(list2.val)
            p2 = p2.next

        p = res_list
        while p1 and p2:
            if p1.val < p2.val:
                p.next = ListNode(p1.val)
                p = p.next
                p1 = p1.next
            else:
                p.next = ListNode(p2.val)
                p = p.next
                p2 = p2.next

        if p1:
            p.next = p1
        else:
            p.next = p2

        return res_list