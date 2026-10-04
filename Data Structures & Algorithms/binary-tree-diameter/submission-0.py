# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, node: TreeNode | None) -> int:
        # we start one because we count ourselves
        d_left = 0
        d_right = 0
        if node.left:
            d_left = self.depth(node.left)
        if node.right:
            d_right = self.depth(node.right)
        
        self.max_diameter = max(self.max_diameter, d_left + d_right)

        return 1 + max(d_left, d_right)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            self.max_diameter = 0
            self.depth(root)
            return self.max_diameter
        else:
            return 0
            