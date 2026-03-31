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
        
        cur1, cur2, newlist = list1, list2, None
        head = None

        while cur1 or cur2:
            if not cur2 or (cur1 and cur1.val <= cur2.val):
                if not newlist:
                    newlist = ListNode(cur1.val)
                    head = newlist
                else:
                    newlist.next = ListNode(cur1.val)
                    newlist = newlist.next
                cur1 = cur1.next
            else:
                if not newlist:
                    newlist = ListNode(cur2.val)
                    head = newlist
                else:
                    newlist.next = ListNode(cur2.val)
                    newlist = newlist.next
                cur2 = cur2.next

        return head