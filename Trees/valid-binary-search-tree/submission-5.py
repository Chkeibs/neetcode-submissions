class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        values = []

        def inorder(node):
            if not node:
                return

            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)

        for i in range(1, len(values)):
            if values[i] <= values[i - 1]:
                return False

        return True