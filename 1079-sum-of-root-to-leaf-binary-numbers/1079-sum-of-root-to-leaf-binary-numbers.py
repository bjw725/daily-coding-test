class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, current):
            if not node:
                return 0

            # 現在のビットを左にシフトして追加（2進数の構築）
            current = (current << 1) | node.val

            # 葉ノードなら現在の数値を返す
            if not node.left and not node.right:
                return current

            # 左右の子を探索し、合計を返す
            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)