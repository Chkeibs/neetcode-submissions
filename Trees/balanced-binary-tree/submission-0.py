# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)

            return 1 + max(left_height,right_height)
        if not root:
            return True
        if abs(height(root.left)-height(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        