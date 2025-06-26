class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0
            # 左右の部分木の合計値を再帰的に取得
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            # 現在ノードのチルトを加算
            self.total_tilt += abs(left_sum - right_sum)
            # このノードを根とする部分木の合計値を返す
            return node.val + left_sum + right_sum

        dfs(root)
        return self.total_tilt