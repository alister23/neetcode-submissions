# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def equal(self, root, other):
        if not other and root:
            return False
        if not root and other:
            return False
        if not root and not other:
            return True
        return root.val == other.val and self.equal(root.left, other.left) and self.equal(root.right, other.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and root:
            return False
        if not root and subRoot:
            return False
        if not subRoot and not root:
            return True
        # print(root.val, subRoot.val)
        if root.val == subRoot.val:
            if self.equal(root.left, subRoot.left) and self.equal(root.right, subRoot.right):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)