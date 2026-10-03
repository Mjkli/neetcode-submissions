# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flip(self, root: TreeNode, queue: List):
        if root.left != None:
            queue.append(root.left)
        if root.right != None:
            queue.append(root.right)
        temp = root.right
        root.right = root.left
        root.left = temp

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = []
        if root != None:
            queue.append(root)
        while len(queue) > 0:
            self.flip(queue.pop(0), queue)
        
        return root
