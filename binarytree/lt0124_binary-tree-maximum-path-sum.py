"""
recursion, help function returns left, right, left and right path sum, record the maximum of each call

Time complexity: O(n), n is the # of nodes
Space complexity:  O(1)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        ret = [-float('INF')]
        def maxnode(root): # return a list, max root with left path, max root with right path, max root with both path
            if not root:
                return [0, 0, 0]
            max_left = max(0, max(maxnode(root.left)[:2],) )
            max_right = max(0, max(maxnode(root.right)[:2 ]))
            ret[0] = max([ret[0], max_left + root.val, max_right + root.val, max_left + max_right + root.val])
            return [max_left + root.val, max_right + root.val, max_left + max_right + root.val]
        maxnode(root)
        return ret[0]
