class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # ヘルパー関数：一番左下まで行ったときの深さを返す
        def getDepth(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth

        # 木が空だったらノード数は0
        if not root:
            return 0

        # 左部分木と右部分木の深さをそれぞれ求める
        left_depth = getDepth(root.left)
        right_depth = getDepth(root.right)

        # 左右の深さが同じなら、左側は完全な2^d - 1個のノードを持つ
        if left_depth == right_depth:
            # 左のノード数 + 再帰的に右を探索 + 自分の分(1)
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # 右の深さが浅いなら、右側は完全木で、左を再帰的に探索
            return (1 << right_depth) + self.countNodes(root.left)