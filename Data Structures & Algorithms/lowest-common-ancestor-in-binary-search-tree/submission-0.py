class Solution:
    def lowestCommonAncestor(self, root, p, q):
        node = root

        while node is not None:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node