class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return
            # 左の部分木を先にたどる
            dfs(node.left)
            # 次に右の部分木
            dfs(node.right)
            # 最後に自分（根）を追加
            result.append(node.val)

        dfs(root)
        return result