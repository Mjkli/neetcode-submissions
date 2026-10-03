# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, p_node: Optional[TreeNode], q_node: Optional[TreeNode], p_stack: [], q_stack:[]) -> bool:
        
        if p_node != None and q_node == None:
            return False
        elif p_node == None and q_node != None:
            return False
        elif p_node == None and q_node == None:
            return True
        elif p_node.val != q_node.val:
            return False
        
        p_stack.append(p_node.left)
        p_stack.append(p_node.right)
        q_stack.append(q_node.left)
        q_stack.append(q_node.right)
        
        while len(p_stack) > 0 and len(q_stack) > 0:
            if not self.traverse(p_stack.pop(), q_stack.pop(), p_stack, q_stack):
                return False
        
        return True
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            return self.traverse(p, q, [], [])