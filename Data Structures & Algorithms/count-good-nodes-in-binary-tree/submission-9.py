# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node: TreeNode, max_path: int):
        if node:
            if node.val >= max_path:
                self.good_nodes += 1
                max_path = node.val

            if node.left:
                self.traverse(node.left, max_path)
            if node.right:
                self.traverse(node.right, max_path)


    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes = 0
        self.traverse(root, root.val)
        return self.good_nodes
