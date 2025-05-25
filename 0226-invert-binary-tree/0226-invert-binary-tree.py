class Solution(object):
    def invertTree(self, root):

        # ノードが空ならそのままNoneを返す
        if not root:
            return None

        # 左右の子ノードを再帰的に反転
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # 反転した結果を左右入れ替える
        root.left = right
        root.right = left

        # 自分自身（root）を返す
        return root