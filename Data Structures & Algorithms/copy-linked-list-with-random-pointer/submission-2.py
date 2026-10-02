"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        index_map = {}
        out = []
        ptr = head
        while ptr != None:
            new_node = Node(ptr.val)
            if len(out) != 0:
                out[-1].next = new_node

            out.append(new_node)
            index_map[ptr] = new_node
            ptr = ptr.next
   
        ptr = head
        while ptr != None:
            if ptr.random != None:
                index_map[ptr].random = index_map[ptr.random]
            
            

            
            ptr = ptr.next

        if len(out) > 0:
            return out[0]
        return None