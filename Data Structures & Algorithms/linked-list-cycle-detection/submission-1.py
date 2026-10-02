# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_map = {}
        l_ptr = head
        while l_ptr != None and l_ptr not in node_map.keys():
            node_map[l_ptr] = l_ptr.val
            l_ptr = l_ptr.next
        
        if l_ptr == None:
            return False
        else:
            return True
