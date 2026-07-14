# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depths = {}

    def maxDepth(self, root):
        if root in Solution.max_depths:
            return Solution.max_depths[root]
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        ans = 1 + max(left, right)
        Solution.max_depths[root] = ans
        return ans

    def diameter(self, node):
        if not node:
            return 0
        return self.maxDepth(node.left) + self.maxDepth(node.right)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_diameter = max(self.diameter(root), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max_diameter
        