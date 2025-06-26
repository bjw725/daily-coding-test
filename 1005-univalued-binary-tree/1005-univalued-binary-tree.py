class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, val):
            if not node:
                return True
            if node.val != val:
                return False
            return dfs(node.left, val) and dfs(node.right, val)

        return dfs(root, root.val)