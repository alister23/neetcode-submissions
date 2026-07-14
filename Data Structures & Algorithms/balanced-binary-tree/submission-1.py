# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    heights = {}

    def getHeight(self, root):
        if not root:
            return 0
        if root in Solution.heights:
            return Solution.heights[root]
        height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        Solution.heights[root] = height
        return height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.getHeight(root.left)-self.getHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)