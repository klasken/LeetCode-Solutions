# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        courant = dummy
        while list1 and list2:
            if list1.val < list2.val:
                courant.next = list1
                list1 = list1.next
            else:
                courant.next = list2
                list2 = list2.next
            courant = courant.next
        if list1:
            courant.next = list1
        elif list2:
            courant.next = list2
        return dummy.next
