# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def downALevel(self, root: TreeNode | None) -> int:
        if root == None:
            return 0

        left_depth = self.downALevel(root.left)
        right_depth = self.downALevel(root.right)

        return 1 + max(left_depth, right_depth)

            
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root != None:
            return self.downALevel(root)

        return 0
