class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # 葉ノードに到達して、残りのtargetSumと値が一致すればTrue
        if not root.left and not root.right:
            return targetSum == root.val

        # 左右の部分木で再帰的に探索
        return (
            self.hasPathSum(root.left, targetSum - root.val) or
            self.hasPathSum(root.right, targetSum - root.val)
        )