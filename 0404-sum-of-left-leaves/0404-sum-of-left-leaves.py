class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        total = 0

        # 左の子が葉かどうかを確認
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val

        # 左右の部分木を再帰的に探索
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)

        return total