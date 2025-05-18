class Solution:
    def kWeakestRows(self, mat, k):
        # 各行ごとに、(兵士の数, 行番号) を作る
        row_strength = []

        for i, row in enumerate(mat):
            # 行の中で1の数（兵士の数）を数える
            soldier_count = row.count(1)
            row_strength.append((soldier_count, i))

        # 兵士の数 → 行番号の順でソート
        row_strength.sort()

        # k個分の行番号だけ取り出して返す
        return [i for _, i in row_strength[:k]]