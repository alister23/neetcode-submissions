# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < q.val:
            less = p.val
            more = q.val
        else:
            less = q.val
            more = p.val
        cur = root
        while cur and not less <= cur.val <= more:
            if less <= cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return cur
