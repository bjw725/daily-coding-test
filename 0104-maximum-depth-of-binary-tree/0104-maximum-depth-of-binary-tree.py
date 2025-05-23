class Solution(object):
    def maxDepth(self, root):
        # ノードが空（None）だったら深さは0
        if root is None:
            return 0

        # 左右の深さを再帰的に計算して、深い方に1を足す
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1