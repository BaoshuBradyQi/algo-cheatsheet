"""
using pre-order traversal to determine if a tree is the same as the other
keep that in a dictionary to check duplicity

Time complexity: O(n)
Space complexity: depends on return, could be O(n ^ 2) for the worst case (no dup)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        node_d = dict()
        ret = set()
        def preorder(root):
            if not root:
                return "##"
            left_node = preorder(root.left)
            right_node = preorder(root.right)

            tr = "{},{},{}".format(root.val, left_node, right_node)
            if tr in node_d:
                ret.add(tr)
            else:
                node_d[tr] = root
            return tr
        preorder(root)
        return [node_d[k] for k in ret]

