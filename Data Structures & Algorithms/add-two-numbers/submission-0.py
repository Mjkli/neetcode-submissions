# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []

        ptr1 = l1
        ptr2 = l2

        while ptr1 != None or ptr2 != None:
            if ptr1 != None:
                stack1.append(ptr1.val)
                ptr1 = ptr1.next
            if ptr2 != None:
                stack2.append(ptr2.val)
                ptr2 = ptr2.next
        
        num1 = []
        num2 = []
        while len(stack1) > 0 or len(stack2) > 0:
            if len(stack1) > 0:
                num1.append(stack1.pop())
            if len(stack2) > 0:
                num2.append(stack2.pop())

        num1 = int("".join(map(str,num1)))
        num2 = int("".join(map(str,num2)))

        total = num1 + num2
        total = str(total)
        total_stack = []
        for char in total:
            total_stack.append(int(char))
        
        base = None
        ptr = None
        print(total_stack)
        while len(total_stack) > 0:
            new_node = ListNode(total_stack.pop())
            if base == None:
                ptr = new_node
                base = new_node
            else:
                ptr.next = new_node
                ptr = ptr.next


        return base
