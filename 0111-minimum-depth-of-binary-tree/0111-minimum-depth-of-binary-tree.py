class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # どちらか一方の子がない場合、存在する方の深さを使う
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        # 両方の子がある場合、最小深さを取る
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))