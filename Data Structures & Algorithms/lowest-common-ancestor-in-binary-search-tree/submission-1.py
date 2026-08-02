# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = []
        cur = root
        while cur != p:
            p_ancestors.append(cur)
            if cur.val > p.val:
                cur = cur.left
            else:
                cur = cur.right
        p_ancestors.append(p)

        q_ancestors = []
        cur = root
        while cur != q:
            q_ancestors.append(cur)
            if cur.val > q.val:
                cur = cur.left
            else:
                cur = cur.right
        q_ancestors.append(q)

        ancestor = None

        for i in range(min(len(p_ancestors), len(q_ancestors))):
            if p_ancestors[i] == q_ancestors[i]:
                ancestor = p_ancestors[i]

        return ancestor