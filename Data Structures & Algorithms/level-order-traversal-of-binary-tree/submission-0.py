# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node: TreeNode, level: int):
        if len(self.level_node) <= level:
            self.level_node.append([node.val])
        else:
            self.level_node[level].append(node.val)
        

        if node.left:
            self.traverse(node.left, level + 1)
        
        if node.right:
            self.traverse(node.right, level + 1)



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level_node = []
        if root:
            self.traverse(root, 0)
            
        return self.level_node