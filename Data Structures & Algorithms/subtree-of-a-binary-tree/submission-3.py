# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validate(self, node: TreeNode, subRoot: TreeNode) -> bool:
        
        if node == None and subRoot == None:
            return True
        elif (node != None and subRoot == None) or (node == None and subRoot != None):
            return False

        if node.val != subRoot.val:
            return False

        return self.validate(node.left, subRoot.left) and self.validate(node.right, subRoot.right)
        

    def traverse(self, node: Optional[TreeNode], subRoot: TreeNode, queue: List) -> bool:
        if node.val == subRoot.val and self.validate(node, subRoot):
            return True
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
        while queue:
            res = self.traverse(queue.pop(0), subRoot, queue)
            if res:
                return True
    
        return False

        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            return self.traverse(root, subRoot, [])
        elif root and not subRoot:
            return False
        else:
            return True