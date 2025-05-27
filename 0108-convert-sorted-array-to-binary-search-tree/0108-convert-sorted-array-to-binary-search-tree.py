class Solution(object):
    def sortedArrayToBST(self, nums):

        # 空リストならNone（空の木）を返す
        if not nums:
            return None

        # 中央のインデックスを取る（ここがルートになる）
        mid = len(nums) // 2

        # 中央の値でノードを作る
        root = TreeNode(nums[mid])

        # 左半分を使って左の部分木を再帰的に構築
        root.left = self.sortedArrayToBST(nums[:mid])

        # 右半分を使って右の部分木を再帰的に構築
        root.right = self.sortedArrayToBST(nums[mid+1:])

        # 最終的なルートノードを返す
        return root