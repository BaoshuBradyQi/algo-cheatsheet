"""
dp solution, maintain a list of taking vs not taking root value
time complexity: O(n)
space complexity: O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def rob_tree(r):
            if not r:
                return [0, 0]
            left = rob_tree(r.left)
            right = rob_tree(r.right)
            return [r.val + left[1] + right[1], max(left) + max(right)]
        return max(rob_tree(root))

