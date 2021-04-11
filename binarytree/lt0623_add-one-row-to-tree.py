"""
recursive
if depth is more than 2, it would become add to left/right node with depth - 1
corner cases would be depth == 1, in which root would become left child
and when depth == 2,  would add to both left and right child

time complexity would be O(n)
space complexity would be O(1)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val, root)
        elif depth == 2:
            root.left  = TreeNode(val,  root.left)
            root.right = TreeNode(val, right=root.right)
            return root
        else:
            if root.left is not None:
                root.left = self.addOneRow(root.left, val, depth - 1)
            if root.right is not None:
                root.right = self.addOneRow(root.right, val, depth - 1)
            return root
