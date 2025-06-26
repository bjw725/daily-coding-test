class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            # 左右のサブツリーの深さを再帰的に計算
            left = depth(node.left)
            right = depth(node.right)
            # このノードを通るパスの長さ（辺の数）＝ left + right
            self.max_diameter = max(self.max_diameter, left + right)
            # 高さを返す（親ノードのため）
            return max(left, right) + 1

        depth(root)
        return self.max_diameter