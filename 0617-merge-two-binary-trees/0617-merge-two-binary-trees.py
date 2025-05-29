# TreeNode クラスの定義（LeetCodeでは最初から与えられる）
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):

        # 両方None → 何もマージするものがないのでNoneを返す
        if not root1 and not root2:
            return None

        # 片方がNone → 残ってる方を使う
        if not root1:
            return root2
        if not root2:
            return root1

        # 両方にノードがある → 値を足して新しいノードを作る
        merged = TreeNode(root1.val + root2.val)

        # 左右の子ノードも同じように再帰でマージ
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)

        return merged