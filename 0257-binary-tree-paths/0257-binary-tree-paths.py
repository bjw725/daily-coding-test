class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        result = []

        def dfs(node, path):
            if not node.left and not node.right:
                # 葉ノードに到達 → パスを結果に追加
                result.append(path)
                return
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))

        # 初期呼び出し（ルートの値からスタート）
        dfs(root, str(root.val))
        return result