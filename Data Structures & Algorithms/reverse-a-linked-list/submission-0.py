# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        follow = head
        if head == None:
            return follow
        lead = head.next
        follow.next = None
        while lead != None:
            temp = lead.next
            lead.next = follow
            follow = lead
            lead = temp

        return follow
