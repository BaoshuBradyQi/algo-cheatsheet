"""
it is easy to determine which node to delete, the key point is how to delete them while continuing the recursion

Time complexity: O(# of nodes)
Space complexity: O(# of to delete nodes)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        ret = list()
        candi = set(to_delete)
        def delete_node(root, is_root):
            if not root:
                return None
            if is_root and root.val not in candi:
                ret.append(root)
            root.left = delete_node(root.left, root.val in candi)
            root.right = delete_node(root.right, root.val in candi)
            return None if root.val in candi else root
        delete_node(root, True)
        return ret
