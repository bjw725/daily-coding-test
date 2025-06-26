class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        num_rows = len(strs)
        num_cols = len(strs[0])
        delete_count = 0

        # 各列（インデックス j）をチェック
        for j in range(num_cols):
            for i in range(1, num_rows):
                # 上の行より小さい → 辞書順でない → 削除対象
                if strs[i][j] < strs[i - 1][j]:
                    delete_count += 1
                    break  # この列は削除対象、次の列へ
        return delete_count