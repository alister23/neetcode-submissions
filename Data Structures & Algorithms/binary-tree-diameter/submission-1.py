# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        diameter = 0
        def getHeight(r):
            nonlocal diameter
            if not r:
                return -1
            left = getHeight(r.left)
            right = getHeight(r.right)
            diameter = max(diameter, left+right+2)
            return max(left, right)+1

        diameter = max(getHeight(root), diameter)
        return diameter

        


        