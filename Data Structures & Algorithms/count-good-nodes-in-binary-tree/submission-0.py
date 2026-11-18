class Solution:
    def goodNodes(self, root):
        def dfs(node, max_so_far):
            if node is None:
                return 0

            good_here = 1 if node.val >= max_so_far else 0
            path_max = max(max_so_far, node.val)

            left_count = dfs(node.left, path_max)
            right_count = dfs(node.right, path_max)

            return good_here + left_count + right_count

        return dfs(root, float("-inf"))